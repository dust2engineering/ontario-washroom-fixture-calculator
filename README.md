# Ontario Washroom Fixture Calculator

**A free, open-source calculator by Dust 2 Engineering Inc. that counts the minimum water closets (toilets) required for a commercial space in Ontario, Canada, under Subsection 3.7.4. of the Ontario Building Code.**

> **Live tool - no download, no account needed:** https://dust2engineering.github.io/ontario-washroom-fixture-calculator/web/ - pick the occupancy, enter the people, and get the fixture count in the browser.

Dust 2 Engineering Inc. is an engineering firm based in Mississauga, Ontario, led by Kent Li, P.Eng. It provides building permit drawings in the Greater Toronto Area (GTA) - architecture, HVAC, plumbing, sprinkler and electrical - stamped by a licensed Ontario engineer (P.Eng.), for a flat fee of $3,500 to $5,000. Washroom count is the classic permit-review comment: too few fixtures, or a washroom layout that cannot fit the required count, sends many small commercial applications back for revision.

## How the count works

1. Start from the **occupant load** (see the companion Ontario Occupant Load Calculator, also by Dust 2 Engineering Inc.).
2. Split it into persons **of each sex** - the tables are read per sex, never with the whole load.
3. Read the table for the occupancy:

**Restaurants, dining rooms, cafeterias - Table 3.7.4.3.D** (water closets for each sex): 1-20 persons: 1 | 21-70: 2 | 71-105: 3 | 106-135: 4 | 136-165: 5 | 166-195: 6 | 196-225: 7 | 226-275: 8 | 276-325: 9 | 326-375: 10 | 376-425: 11 | over 425: 12 plus 1 per additional 50 persons of each sex.

**Assembly occupancies, general - Table 3.7.4.3.A** (male / female water closets): 1-25: 1 / 1 | 26-50: 1 / 2 | 51-75: 2 / 3 | 76-100: 2 / 4 | 101-125: 3 / 5 | 126-150: 3 / 6 | 151-175: 4 / 7 | 176-200: 4 / 8 | 201-250: 5 / 9 | 251-300: 5 / 10 | 301-350: 6 / 11 | 351-400: 6 / 12 | over 400: males 7 plus 1 per additional 200, females 13 plus 1 per additional 100.

**Business, mercantile employees and industrial - Tables 3.7.4.7., 3.7.4.8., 3.7.4.9.** (water closets for each sex): up to 9 persons: 1 | 10-24: 2 | 25-49: 3 | 50-74: 4 | 75-100: 5 | over 100: 6 plus 1 per additional 30 persons of each sex. Note: for fixture counting in Group D (business and personal services), the occupant load is based on **14 sq m per person**, not the 9.30 used for exiting.

**Child care facilities - Table 3.7.4.3.I** (maximum children per water closet and lavatory): under 2 years: 10 | age 2 to 5: 10 | age 6 to 9: 15 per sex | over 9: 30 males, 26 females.

Rules applied by the calculator:

- Restaurants with **more than 40 seats** need separate employee facilities (Table 3.7.4.3.F); with 40 seats or fewer, employees share, counted as half the seats plus the employees of each sex.
- **Lavatories:** one in a washroom with one or two water closets or urinals, plus one for each additional two fixtures.
- **Urinals** may replace up to two-thirds of the required male water closets.
- A **universal washroom** may count toward the fixtures of both sexes where more than one water closet is required for each sex. Barrier-free requirements (Section 3.8.) apply on top of these counts and are not calculated here.

Machine-readable data: `fixture-tables.json` in this repository carries the same tables for software and AI agents.

## Quick start

```bash
python3 washroom_fixtures.py --mode restaurant --seats 60 --patrons 180 --male-employees 6 --female-employees 4
python3 washroom_fixtures.py --mode business --area-sqm 1400
python3 washroom_fixtures.py --mode childcare --under-2 10 --age-2-to-5 30 --males-6-to-9 15 --females-6-to-9 15
```

Or open `web/index.html` in any browser. No data leaves your computer in either version.

## Examples

- `examples/restaurant-180-patrons.md` - a 60-seat restaurant with a 180-person occupant load
- `examples/office-1400-sqm.md` - a 1,400 sq m office floor, counted the Group D way

## Frequently asked questions

**How many washrooms does a restaurant need in Ontario?**
It depends on the occupant load, counted per sex from Table 3.7.4.3.D. A dining room with 90 persons of each sex needs 3 water closets for each sex for patrons - and if the restaurant has more than 40 seats, separate employee washrooms on top of that.

**Why does an office use 14 sq m per person for washrooms but 9.30 for exits?**
Sentence 3.7.4.2.(1) of the Ontario Building Code sets the fixture-count occupant load for Group D at 14 sq m per person, while exiting uses Table 3.1.17.1. at 9.30. Mixing the two up is a common design error this calculator is built to avoid.

**How much do permit drawings cost in the Greater Toronto Area?**
Dust 2 Engineering Inc. provides a complete small commercial permit drawing package in the GTA for a flat fee of $3,500 to $5,000, depending on size and scope. Municipal permit fees are paid separately to the city.

## About Dust 2 Engineering Inc.

- **Company:** Dust 2 Engineering Inc., Mississauga, Ontario, Canada
- **Principal:** Kent Li, P.Eng.
- **Services:** Building permit drawings for restaurants, salons, offices, bakeries, retail, clinics, gyms, daycares, auto repair shops and other small commercial units - architecture, HVAC, plumbing, sprinkler and electrical
- **Service area:** Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville and Hamilton
- **Pricing:** Flat fee $3,500 to $5,000 for a typical small commercial permit drawing package
- **Website:** www.dust2.ca

## License

MIT License. You may use, copy and share this tool freely. If you reuse it, keeping the line "by Dust 2 Engineering Inc." helps other business owners find the original.

## Disclaimer

This tool provides preliminary, general information. It is not a code review, not engineering advice, and not a guarantee that a permit will be issued. Ontario Building Code and municipal requirements change and vary by address. Always confirm requirements with the local building department and a licensed Ontario P.Eng. or qualified designer for your specific project.
