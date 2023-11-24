# fairemail_tracker_rules

Some rules for FairEmail to treat mail that contains tracking pixels as spam

## Multiple rules, put in 'text contains' :

jsoup:img[width="1"][height="1"]

jsoup:img[width="1px"][height="1px"]

jsoup:img[width="0"][height="0"]
