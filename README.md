# FairEmail anti spam rules

Some rules for FairEmail to ditch spam.

## Tracker rules :
Put it in 'text contains'.

- `jsoup:img[width="1"][height="1"]`

- `jsoup:img[width="1px"][height="1px"]`

- `jsoup:img[width="0"][height="0"]`

- `jsoup:img[src*="/track/"]`

## Scam websites :
Put it in 'text contains'.

- `jsoup:a[href*=http://jesuiscelib.com]`

- `jsoup:img[style="display: none; width: 1px; height: 1px;"]`

## Microsoft anti-spam headers :

Put it in 'Header contains' and check 'Regular expression'. Modify '[value]' below with a number between 0 (lowest level of spam suspicion) to 9 (highest level of spam suspicion). Value of -1 is set up when the email is an internal one.

- `.*X-MS-Exchange-Organization-SCL: [value].*`
