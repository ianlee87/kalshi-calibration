# Kalshi Calibration
Kalshi, along with many other prediction markets operate in a system similar to this: at a 30¢, the traders are saying there is a 30% chance. This project will test whether if this is true by analyzing thousands of settled markets across Kalshi, and these observations will get visualized as charts where perfectly calibrated markets fall right on the diagonal line.

## Results

![Calibration chart](calibration.png)

Across 804 settled NYC and Chicago high-temperature markets, cheap contracts (under 40¢) won less often than their price implied, and 40–60¢ favorites won more often. That's a classic favorite-longshot bias. Markets priced 60¢ and up are grouped into one bucket because there are only 8 of them.

### Brier Score


Lower is better. Always guessing 50¢ would score 0.25.
| Series | Markets | Brier score |
|---|---|---|
| NYC (KXHIGHNY) | 402 | 0.0951 |
| Chicago (KXHIGHCHI) | 402 | 0.1066 |