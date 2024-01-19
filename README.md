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
