# polybar-indodax

> Forked from [willHol/polybar-crypto](https://github.com/willHol/polybar-crypto) to suit the Indodax API.

A *polybar script* that displays the price of various **crypto-currencies**.

![both](https://user-images.githubusercontent.com/1184957/110332836-73e59a00-8053-11eb-8cbf-ce6ebbbc0ccf.png)

## Setup
```bash
mkdir -p ~/.config/polybar/scripts &&
    cd ~/.config/polybar/scripts &&
    git clone https://github.com/ditatompel/polybar-indodax.git &&
    cd polybar-indodax &&
    mv config_sample config
```

Then in `~/.config/polybar/config`:

```ini
[bar/top]

...

modules-right = crypto

...

[module/crypto]
type = custom/script
interval = 60
exec = /home/<user>/.config/polybar/scripts/polybar-indodax/indodax.py

```

## Example Configuration

`~/.config/polybar/scripts/polybar-indodax/config`
```ini
[general]
; Information displayed on Polyfill. can be both, percentage, or price.
; default: both
display = both

; Use hexadecimal color code, Polybar alpha value is supported
color_symbol = #0a81f5
color_down = #ff2424
color_up = #00ff84

; begin list of cryptocurrency
[btc_idr]
symbol = BTC

[ada_idr]
symbol = ADA

[eth_idr]
symbol = ETH

[xmr_idr]
symbol = XMR

```

### Display Modes

`display = percentage`

![percentage](https://user-images.githubusercontent.com/1184957/110332713-47318280-8053-11eb-8056-2bca58c6f799.png)

`display = price`

![price](https://user-images.githubusercontent.com/1184957/110332913-8eb80e80-8053-11eb-945a-8d7aaa492c70.png)

`display = both`

![both](https://user-images.githubusercontent.com/1184957/110332836-73e59a00-8053-11eb-8cbf-ce6ebbbc0ccf.png)

## Notes
> I don't work or have any affiliate with official Dompet Bitcoin Indonesia or INDODAX Trading Platform. This program is free software and distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
