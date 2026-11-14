# Worked example - 60-seat restaurant, 180-person occupant load

Inputs: 60 seats, patron occupant load 180 (90 of each sex), 6 male and 4 female employees at one time.

- Patrons (Table 3.7.4.3.D): 90 persons of each sex falls in the 71-105 row: **3 water closets for each sex**. Lavatories: 3 fixtures need 2 lavatories per sex. Up to 2 of the 3 male water closets may be urinals.
- Employees: more than 40 seats, so separate employee facilities are required (Table 3.7.4.3.F): 6 male employees and 4 female employees each fall in the 1-9 row: **1 water closet and 1 lavatory for each sex**.
- **Total: 8 water closets.**

Reproduce it: `python3 washroom_fixtures.py --mode restaurant --seats 60 --patrons 180 --male-employees 6 --female-employees 4`

Preliminary information only, by Dust 2 Engineering Inc., Mississauga - verify with your designer and the local building department.
