# Suricata Alert-Debug.log Transformation for Machine Learning

Welcome to this repository! Here, we focus on a not-so-common yet incredibly useful logging feature of Suricata: the `alert-debug.log`. This verbose log file, often overlooked, is a goldmine for machine learning experiments. 

## Features

- **Alert-Debug.log to CSV Conversion**: We provide scripts that efficiently transform the typically cluttered `alert-debug.log` into a clean and structured CSV format. This conversion is essential for making the data amenable to machine learning algorithms.

- **Real-World Data Sample**: To add a touch of realism and enhance the learning experience, I've included a sample `alert-debug.log` file (see: logs_suricata). This sample was captured by running a honeypot (T-Pot) on AWS. It's a practical example to see how real-world data looks and behaves.

## Advantages

- **Pcap Data Analysis**: One of the major benefits of this conversion is the facilitation of pcap header and payload data analysis, particularly in hexadecimal format. This is a crucial aspect for advanced network data analysis and cybersecurity applications.

## Getting Started

To begin, first clone this repository. After cloning, execute `parser.py` followed by `2csv.py` to initiate the data transformation process.

Happy Experimenting!


```
Example of alert-debug.log
+================
TIME:              12/21/2023-05:51:36.729125
PKT SRC:           wire/pcap
SRC IP:            162.216.149.209
DST IP:            11.2.1.141
PROTO:             6
SRC PORT:          63168
DST PORT:          2280
TCP SEQ:           2401199204
TCP ACK:           1783044834
FLOW:              to_server: TRUE, to_client: FALSE
FLOW Start TS:     12/21/2023-05:51:35.528353
FLOW PKTS TODST:   5
FLOW PKTS TOSRC:   4
FLOW Total Bytes:  643
FLOW IPONLY SET:   TOSERVER: TRUE, TOCLIENT: TRUE
FLOW ACTION:       DROP: FALSE
FLOW NOINSPECTION: PACKET: FALSE, PAYLOAD: FALSE, APP_LAYER: FALSE
FLOW APP_LAYER:    DETECTED: TRUE, PROTO 5
PACKET LEN:        66
PACKET:
 0000  02 8B C2 CC 86 87 02 9B  30 A5 76 E8 08 00 45 00   ........ 0.v...E.
 0010  00 34 DE 48 40 00 37 06  20 43 A2 D8 95 D1 0B 02   .4.H@.7.  C......
 0020  01 8D F6 C0 08 E8 8F 1F  64 64 6A 47 1A E2 80 11   ........ ddjG....
 0030  01 FF EF C0 00 00 01 01  08 0A 79 12 AE 58 52 0C   ........ ..y..XR.
 0040  4D F6                                              M.
ALERT CNT:           1
ALERT MSG [00]:      ET POLICY SSH session in progress on Unusual Port
ALERT GID [00]:      1
ALERT SID [00]:      2001984
ALERT REV [00]:      9
ALERT CLASS [00]:    Misc activity
ALERT PRIO [00]:     3
ALERT FOUND IN [00]: PACKET
ALERT IN TX [00]:    N/A
+================
```

```
...and after the log is turned to CSV....
Packet Data,Alert SID,Alert REV,Payload Data
02 8B C2 CC 86 87 02 9B  30 A5 76 E8 08 00 45 00 00 34 DE 48 40 00 37 06  20 43 A2 D8 95 D1 0B 02 01 8D F6 C0 08 E8 8F 1F  64 64 6A 47 1A E2 80 11 01 FF EF C0 00 00 01 01  08 0A 79 12 AE 58 52 0C 4D F6,2001984,9,
33 33 00 01 00 02 02 8B  C2 CC 86 87 86 DD 60 0F 13 73 00 40 11 01 FE 80  00 00 00 00 00 00 00 8B C2 FF FE CC 86 87 FF 02  00 00 00 00 00 00 00 00 00 00 00 01 00 02 02 22  02 23 00 40 92 46 01 47 8E E3 00 01 00 0E 00 01  00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06 00 08  00 17 00 18 00 27 00 1F 00 08 00 02 FF FF 00 03  00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,2030387,2,01 47 8E E3 00 01 00 0E  00 01 00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06  00 08 00 17 00 18 00 27 00 1F 00 08 00 02 FF FF  00 03 00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18
02 8B C2 CC 86 87 02 9B  30 A5 76 E8 08 00 45 48 00 34 00 00 40 00 2D 06  C5 ED 82 E7 F8 18 0B 02 01 8D F7 40 FB 27 F8 D0  F6 41 56 88 B5 46 80 11 08 00 2E D6 00 00 01 01  08 0A 0A 7F 36 C5 A5 07 E4 C0,2210037,2,
02 9B 30 A5 76 E8 02 8B  C2 CC 86 87 08 00 45 10 00 34 71 72 40 00 40 06  41 B3 0B 02 01 8D 82 E7 F8 18 FB 27 F7 40 56 88  B5 46 F8 D0 F6 42 80 11 01 D0 34 D0 00 00 01 01  08 0A A5 07 E4 F5 0A 7F 36 C5,2210037,2,
33 33 00 01 00 02 02 8B  C2 CC 86 87 86 DD 60 0F 13 73 00 40 11 01 FE 80  00 00 00 00 00 00 00 8B C2 FF FE CC 86 87 FF 02  00 00 00 00 00 00 00 00 00 00 00 01 00 02 02 22  02 23 00 40 92 46 01 47 8E E3 00 01 00 0E 00 01  00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06 00 08  00 17 00 18 00 27 00 1F 00 08 00 02 FF FF 00 03  00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,2030387,2,01 47 8E E3 00 01 00 0E  00 01 00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06  00 08 00 17 00 18 00 27 00 1F 00 08 00 02 FF FF  00 03 00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18
02 8B C2 CC 86 87 02 9B  30 A5 76 E8 08 00 45 00 00 28 38 96 40 00 76 06  C0 C8 BC 77 42 6B 0B 02 01 8D FC D2 81 3B 77 B5  A5 59 77 B5 A5 59 50 04 00 00 EC 42 00 00 85 49  63 21 00 00,2210051,2,
02 9B 30 A5 76 E8 02 8B  C2 CC 86 87 08 00 45 00 00 28 05 BE 40 00 3F 06  73 87 0B 02 01 8D 71 C9 44 33 00 19 D9 6D 57 93  B2 81 21 98 41 E9 50 10 01 F6 A4 36 00 00,2260002,1,
33 33 00 01 00 02 02 8B  C2 CC 86 87 86 DD 60 0F 13 73 00 40 11 01 FE 80  00 00 00 00 00 00 00 8B C2 FF FE CC 86 87 FF 02  00 00 00 00 00 00 00 00 00 00 00 01 00 02 02 22  02 23 00 40 92 46 01 47 8E E3 00 01 00 0E 00 01  00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06 00 08  00 17 00 18 00 27 00 1F 00 08 00 02 FF FF 00 03  00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,2030387,2,01 47 8E E3 00 01 00 0E  00 01 00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06  00 08 00 17 00 18 00 27 00 1F 00 08 00 02 FF FF  00 03 00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18
33 33 00 01 00 02 02 8B  C2 CC 86 87 86 DD 60 0F 13 73 00 40 11 01 FE 80  00 00 00 00 00 00 00 8B C2 FF FE CC 86 87 FF 02  00 00 00 00 00 00 00 00 00 00 00 01 00 02 02 22  02 23 00 40 92 46 01 47 8E E3 00 01 00 0E 00 01  00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06 00 08  00 17 00 18 00 27 00 1F 00 08 00 02 FF FF 00 03  00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,2030387,2,01 47 8E E3 00 01 00 0E  00 01 00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06  00 08 00 17 00 18 00 27 00 1F 00 08 00 02 FF FF  00 03 00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18
02 8B C2 CC 86 87 02 9B  30 A5 76 E8 08 00 45 60 00 34 82 0A 40 00 37 06  7B C8 A2 D8 96 2A 0B 02 01 8D F4 26 59 9C 65 CD  47 61 A1 FB D5 B4 80 11 01 FF C0 95 00 00 01 01  08 0A 9A 08 FB 32 84 01 E2 B6,2001984,9,
02 8B C2 CC 86 87 02 9B  30 A5 76 E8 08 00 45 60 00 34 32 92 40 00 38 06  C9 CD A2 D8 96 9D 0B 02 01 8D E4 D4 20 3A CC E0  B6 66 7A B3 01 FF 80 11 01 FF 9F 17 00 00 01 01  08 0A BD 07 6E CA C5 96 99 2F,2001984,9,
33 33 00 01 00 02 02 8B  C2 CC 86 87 86 DD 60 0F 13 73 00 40 11 01 FE 80  00 00 00 00 00 00 00 8B C2 FF FE CC 86 87 FF 02  00 00 00 00 00 00 00 00 00 00 00 01 00 02 02 22  02 23 00 40 92 46 01 47 8E E3 00 01 00 0E 00 01  00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06 00 08  00 17 00 18 00 27 00 1F 00 08 00 02 FF FF 00 03  00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,2030387,2,01 47 8E E3 00 01 00 0E  00 01 00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06  00 08 00 17 00 18 00 27 00 1F 00 08 00 02 FF FF  00 03 00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18
```
