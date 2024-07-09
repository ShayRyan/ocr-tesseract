
| WDC State | RC KPI Clock | Effect  |
|:--------|:------- |:------- |
| STBY | RUN  | Start. WDC State >> RUN, WDC = 1, Start Date >> Callback date, Restart Date = None |
| STBY | STOP | Start. WDC State >> STOP, WDC = 0, Start Date >> Callback date, Restart Date = None |
| RUN  | RUN  | Continue @ RUN. WDC State = RUN, WDC = WDC, Restart Date = None |
| RUN  | STOP | STOP. WDC State >> STOP, WDC = WDC, Restart Date = EU Appt Date or None |
| STOP | RUN  | RUN. WDC State >> RUN, WDC = WDC + 1, Restart Date >> Callback date ? None |
| STOP | STOP | Continue @ STOP. WDC State = STOP, WDC = WDC, Update Restart Date with EU Appt Date in callback if later than current restart date |
