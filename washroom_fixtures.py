#!/usr/bin/env python3
"""Ontario Washroom Fixture Calculator - by Dust 2 Engineering Inc., Mississauga, Ontario.
Counts the minimum water closets required by the Ontario Building Code (2024), Division B,
Subsection 3.7.4. - Tables 3.7.4.3.A, 3.7.4.3.D, 3.7.4.3.F, 3.7.4.3.I, 3.7.4.7., 3.7.4.8. and 3.7.4.9.
Preliminary information only. Not engineering advice and not a code review.

Examples:
  python3 washroom_fixtures.py --mode restaurant --seats 60 --patrons 180 --male-employees 6 --female-employees 4
  python3 washroom_fixtures.py --mode assembly --males 90 --females 90
  python3 washroom_fixtures.py --mode business --area-sqm 1400
  python3 washroom_fixtures.py --mode mercantile --male-employees 8 --female-employees 12 --public-males 300 --public-females 300 --area-sqm 800
  python3 washroom_fixtures.py --mode industrial --males 30 --females 10
  python3 washroom_fixtures.py --mode childcare --under-2 10 --age-2-to-5 30 --males-6-to-9 15 --females-6-to-9 15
"""
import argparse

import math
TABLE_A = [(25,1,1),(50,1,2),(75,2,3),(100,2,4),(125,3,5),(150,3,6),(175,4,7),(200,4,8),(250,5,9),(300,5,10),(350,6,11),(400,6,12)]
TABLE_D = [(20,1),(70,2),(105,3),(135,4),(165,5),(195,6),(225,7),(275,8),(325,9),(375,10),(425,11)]
STEPPED = [(9,1),(24,2),(49,3),(74,4),(100,5)]
def table_a(m, f):
    def one(n, sex):
        if n <= 0: return 0
        for lim, mm, ff in TABLE_A:
            if n <= lim: return mm if sex == "m" else ff
        if sex == "m": return 7 + math.ceil((n - 400) / 200)
        return 13 + math.ceil((n - 400) / 100)
    return one(m, "m"), one(f, "f")
def table_d(n):
    if n <= 0: return 0
    for lim, v in TABLE_D:
        if n <= lim: return v
    return 12 + math.ceil((n - 425) / 50)
def stepped(n):
    if n <= 0: return 0
    for lim, v in STEPPED:
        if n <= lim: return v
    return 6 + math.ceil((n - 100) / 30)
def lavatories(fixtures):
    if fixtures <= 0: return 0
    return 1 + math.ceil(max(0, fixtures - 2) / 2)
def max_urinals(male_wc):
    return (male_wc * 2) // 3

FOOT = "Preliminary information only, by Dust 2 Engineering Inc., Mississauga - GTA permit drawings, flat fee $3,500-$5,000, Ontario P.Eng. Barrier-free and universal washroom requirements (OBC Section 3.8.) apply in addition to these counts and are not calculated here."
def main():
    p = argparse.ArgumentParser(description="Ontario washroom fixture calculator (OBC Subsection 3.7.4.) by Dust 2 Engineering Inc.")
    p.add_argument("--mode", required=True, choices=["restaurant", "assembly", "business", "mercantile", "industrial", "childcare"])
    p.add_argument("--seats", type=int, default=0)
    p.add_argument("--patrons", type=int, default=0, help="Patron occupant load (default: same as seats)")
    p.add_argument("--males", type=int, default=0, help="Persons of the male sex (assembly / industrial)")
    p.add_argument("--females", type=int, default=0)
    p.add_argument("--male-employees", type=int, default=0)
    p.add_argument("--female-employees", type=int, default=0)
    p.add_argument("--public-males", type=int, default=0)
    p.add_argument("--public-females", type=int, default=0)
    p.add_argument("--area-sqm", type=float, default=0)
    p.add_argument("--under-2", type=int, default=0)
    p.add_argument("--age-2-to-5", type=int, default=0)
    p.add_argument("--males-6-to-9", type=int, default=0)
    p.add_argument("--females-6-to-9", type=int, default=0)
    p.add_argument("--males-over-9", type=int, default=0)
    p.add_argument("--females-over-9", type=int, default=0)
    a = p.parse_args()
    print("ONTARIO WASHROOM FIXTURE COUNT - OBC SUBSECTION 3.7.4.")
    print("")
    if a.mode == "restaurant":
        patrons = a.patrons if a.patrons > 0 else a.seats
        if a.seats > 40:
            per_sex = math.ceil(patrons / 2)
            wc = table_d(per_sex)
            print("Patrons: occupant load %d, taken as %d of each sex -> Table 3.7.4.3.D: %d water closets for each sex" % (patrons, per_sex, wc))
            print("Patron lavatories (minimum, per sex): %d" % lavatories(wc))
            print("Up to %d of the male patron water closets may be urinals." % max_urinals(wc))
            em, ef = stepped(a.male_employees), stepped(a.female_employees)
            print("More than 40 seats, so employees need separate facilities (Table 3.7.4.3.F): %d water closet(s) and lavatory(ies) for male employees, %d for female employees" % (em, ef))
            print("TOTAL WATER CLOSETS: %d" % (2 * wc + em + ef))
        else:
            ml = math.ceil(a.seats / 2) + a.male_employees
            fl = math.ceil(a.seats / 2) + a.female_employees
            wm, wf = table_d(ml), table_d(fl)
            print("40 seats or fewer, so employees share the patron facilities. Count basis: %d males (half the seats + male employees), %d females" % (ml, fl))
            print("Table 3.7.4.3.D: %d water closets for males, %d for females" % (wm, wf))
            print("TOTAL WATER CLOSETS: %d" % (wm + wf))
    elif a.mode == "assembly":
        wm, wf = table_a(a.males, a.females)
        print("Table 3.7.4.3.A: %d water closets for males, %d for females" % (wm, wf))
        print("Lavatories (minimum): %d male, %d female. Up to %d of the male water closets may be urinals." % (lavatories(wm), lavatories(wf), max_urinals(wm)))
        print("TOTAL WATER CLOSETS: %d" % (wm + wf))
    elif a.mode == "business":
        total = math.ceil(a.area_sqm / 14)
        per_sex = math.ceil(total / 2)
        wc = stepped(per_sex)
        print("Group D fixture counting uses 14 sq m per person: %.0f sq m -> %d persons, taken as %d of each sex" % (a.area_sqm, total, per_sex))
        print("Table 3.7.4.7.: %d water closets for each sex" % wc)
        if total <= 10:
            print("Occupant load is not more than 10, so one water closet may serve both sexes.")
        print("TOTAL WATER CLOSETS: %d" % (2 * wc))
    elif a.mode == "mercantile":
        em, ef = stepped(a.male_employees), stepped(a.female_employees)
        pm = math.ceil(a.public_males / 300) if a.public_males > 0 else 0
        pf = math.ceil(a.public_females / 150) if a.public_females > 0 else 0
        if 0 < a.area_sqm <= 600:
            pm, pf = min(pm, 1), min(pf, 1)
            print("Mercantile area is not more than 600 sq m, so not more than one public water closet per sex is required.")
        print("Employees (Table 3.7.4.8.): %d water closets for males, %d for females" % (em, ef))
        print("Public (1 per 300 males, 1 per 150 females): %d for males, %d for females" % (pm, pf))
        print("Employee water closets may be counted toward the public requirement when they are accessible to the public.")
        print("TOTAL WATER CLOSETS (if counted separately): %d" % (em + ef + pm + pf))
    elif a.mode == "industrial":
        wm, wf = stepped(a.males), stepped(a.females)
        print("Table 3.7.4.9.: %d water closets and %d lavatories for males, %d water closets and %d lavatories for females" % (wm, wm, wf, wf))
        if a.males + a.females <= 10:
            print("Occupant load is not more than 10, so one water closet may serve both sexes.")
        print("TOTAL WATER CLOSETS: %d" % (wm + wf))
    elif a.mode == "childcare":
        u2 = math.ceil(a.under_2 / 10) if a.under_2 > 0 else 0
        a25 = math.ceil(a.age_2_to_5 / 10) if a.age_2_to_5 > 0 else 0
        m69 = math.ceil(a.males_6_to_9 / 15) if a.males_6_to_9 > 0 else 0
        f69 = math.ceil(a.females_6_to_9 / 15) if a.females_6_to_9 > 0 else 0
        m9 = math.ceil(a.males_over_9 / 30) if a.males_over_9 > 0 else 0
        f9 = math.ceil(a.females_over_9 / 26) if a.females_over_9 > 0 else 0
        print("Table 3.7.4.3.I (water closets and lavatories, same count):")
        print("Under 2 years: %d | Age 2 to 5: %d | Age 6 to 9: %d male + %d female | Over 9: %d male + %d female" % (u2, a25, m69, f69, m9, f9))
        print("TOTAL WATER CLOSETS: %d (staff fixtures are counted separately)" % (u2 + a25 + m69 + f69 + m9 + f9))
    print("")
    print(FOOT)
if __name__ == "__main__":
    main()
