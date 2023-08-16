| SkTeil |     condition for Tol     |    mark    |   range   |     mark     |    range    | new |    remark     |
| ------ |:-------------------------:|:----------:|:---------:|:------------:|:-----------:|:---:|:-------------:|
| 1      |             -             | 000.0001mm | ±0.002mm  | 0.000005inch | ±0.0001inch |     |               |
| 2      |             -             | 000.0002mm | ±0.004mm  | 00.00001inch | ±0.0002inch |     |               |
| 3      |       dTol <= 18um        | 000.0005mm | ±0.010mm  | 00.00002inch | ±0.0004inch |     |               |
| 4      |   18 um < dTol ≤ 36 um    | 0000.001mm | ±0.020mm  | 00.00005inch | ±0.001inch  |     |               |
| 5      |   36 um < dTol ≤ 72 um    | 0000.002mm | ±0.040mm  | 00.0001inch  | ±0.002inch  |     |               |
| 6      |   72 um < dTol ≤ 180 um   | 0000.005mm | ±0.100mm  | 00.0002inch  | ±0.004inch  |     |               |
| 7      |  180 um < dTol ≤ 360 um   | 0000.01mm  | ±0.200mm  | 00.0005inch  | ±0.010inch  |     |               |
| 8      |  360 um < dTol ≤ 720 um   | 0000.02mm  | ±0.400mm  |  00.001inch  | ±0.020inch  |     |               |
| 9      |  720 um < dTol ≤ 1800 um  | 0000.05mm  | ±1.000mm  |  00.002inch  | ±0.040inch  |     | only for Tol. |
| 10     | 1800 um < dTol ≤ 3600 um  |  0000.1mm  | ±2.000mm  |  00.005inch  | ±0.100inch  |  X  | only for Tol. |
| 11     | 3600 um < dTol ≤ 7200 um  |  0000.2mm  | ±4.000mm  |  00.01inch   | ±0.200inch  |  X  | only for Tol. |
| 12     | 7200 um < dTol ≤ 18000 um |  0000.5mm  | ±10.000mm |  00.02inch   | ±0.400inch  |  X  | only for Tol. |
| 13     |       18000 < dTol        |  0001.0mm  | ±20.000mm |      -       |      -      |  X  | only for Tol. |
|        |                           |            |           |              |             |     |               |



