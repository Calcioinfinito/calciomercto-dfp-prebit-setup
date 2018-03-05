### Setup DFP


get API key from DFP and put in `key` folder

copy `googleads.example.yaml` to `googleads.yaml` and fill it with right values

fill `settings.py`

run
```
python -m tasks.add_new_prebid_partner
```

**go to dfp panel and approve order**

then run
```
python -m tasks.activate_line_items --orderId=XXX
```