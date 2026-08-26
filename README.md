# Leech Balancer

An [Anki](https://apps.ankiweb.net) add-on that gradually "rehabilitates" leech
cards instead of leaving them flagged forever.

When a card that has previously lapsed is answered correctly N times in a row,
its lapse counter is reduced, so that cards can work their way out of leech status
through good performance alone.

## How It Works

- After every answer, the add-on looks at the card's review history.
- If the card has been answered correctly N times in a row (no "Again" in
  between) the lapse count is reduced by 1.
- Optionally, lapses can be reset straight to 0 instead (see configuration).
- A toast shows when a lapse was reduced or reset (can be disabled).

## Configuration

Open **Tools > Leech Balancer Config**:

- **Required correct answers** (default 3) — consecutive correct answers
  needed before a lapse is reduced.
- **Show toast** (default on) — show a toast notification when a lapse is
  reduced/reset.
- **Reset lapses to zero** (default off) — set the lapse count to 0 instead of
  decrementing it when the threshold is met.

## Credits

Derived from [LeechToolkit](https://github.com/iamjustkoi/LeechToolkit) by
iamjustkoi — thanks for the original add-on.

---

<a href="https://buymeacoffee.com/heigor" alt="Buy Me a Coffee" target="_blank" style="display: block;">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"/>
</a>
<img src="media/bmc_qr.png" alt="Buy Me a Coffee QR" style="display: block; width:170px; margin: 10px 0;"/>
