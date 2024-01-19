# Suricata Alert-Debug.log Transformation for Machine Learning

Welcome to this repository! Here, we focus on a not-so-common yet incredibly useful logging feature of Suricata: the `alert-debug.log`. This verbose log file, often overlooked, is a goldmine for machine learning experiments. 

## Features

- **Alert-Debug.log to CSV Conversion**: We provide scripts that efficiently transform the typically cluttered `alert-debug.log` into a clean and structured CSV format. This conversion is essential for making the data amenable to machine learning algorithms.

- **Real-World Data Sample**: To add a touch of realism and enhance the learning experience, I've included a sample `alert-debug.log` file (see: logs_suricata). This sample was captured by running a honeypot (T-Pot) on AWS. It's a practical example to see how real-world data looks and behaves.

## Advantages

- **Pcap Data Analysis**: One of the major benefits of this conversion is the facilitation of pcap header and payload data analysis, particularly in hexadecimal format. This is a crucial aspect for advanced network data analysis and cybersecurity applications.

## Getting Started

To begin, first clone this repository. After cloning, execute `parser.py` followed by `2csv.py` to initiate the data transformation process. Then unzip the `Tpot_suricata_rules` and run the `merge_4_ML.py` to get the final `mergedML.csv` for your ML experiment.  

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
...and the final output in `mergedML.csv` looks like this....
Packet Data,Alert SID,Alert REV,Payload Data,Suricata_rule
02 8B C2 CC 86 87 02 9B  30 A5 76 E8 08 00 45 00 00 34 DE 48 40 00 37 06  20 43 A2 D8 95 D1 0B 02 01 8D F6 C0 08 E8 8F 1F  64 64 6A 47 1A E2 80 11 01 FF EF C0 00 00 01 01  08 0A 79 12 AE 58 52 0C 4D F6,2001984,9,,"alert ssh any any -> any !$SSH_PORTS (msg:""ET POLICY SSH session in progress on Unusual Port""; flow:established,to_server; threshold: type both, track by_src, count 2, seconds 300; reference:url,doc.emergingthreats.net/2001984; classtype:misc-activity; sid:2001984; rev:9; metadata:created_at 2010_07_30, updated_at 2019_07_26;)"
33 33 00 01 00 02 02 8B  C2 CC 86 87 86 DD 60 0F 13 73 00 40 11 01 FE 80  00 00 00 00 00 00 00 8B C2 FF FE CC 86 87 FF 02  00 00 00 00 00 00 00 00 00 00 00 01 00 02 02 22  02 23 00 40 92 46 01 47 8E E3 00 01 00 0E 00 01  00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06 00 08  00 17 00 18 00 27 00 1F 00 08 00 02 FF FF 00 03  00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,2030387,2,01 47 8E E3 00 01 00 0E  00 01 00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06  00 08 00 17 00 18 00 27 00 1F 00 08 00 02 FF FF  00 03 00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,"alert ipv6 any any -> ff00::/8 any (msg:""ET EXPLOIT Possible CVE-2020-11899 Multicast out-of-bound read"";  reference:url,www.jsof-tech.com/ripple20/; classtype:attempted-admin; sid:2030387; rev:2; metadata:created_at 2020_06_22, former_category EXPLOIT, performance_impact Significant, signature_severity Major, updated_at 2020_08_20;)"
02 8B C2 CC 86 87 02 9B  30 A5 76 E8 08 00 45 48 00 34 00 00 40 00 2D 06  C5 ED 82 E7 F8 18 0B 02 01 8D F7 40 FB 27 F8 D0  F6 41 56 88 B5 46 80 11 08 00 2E D6 00 00 01 01  08 0A 0A 7F 36 C5 A5 07 E4 C0,2210037,2,,"alert tcp any any -> any any (msg:""SURICATA STREAM FIN recv but no session""; stream-event:fin_but_no_session; classtype:protocol-command-decode; sid:2210037; rev:2;)"
02 9B 30 A5 76 E8 02 8B  C2 CC 86 87 08 00 45 10 00 34 71 72 40 00 40 06  41 B3 0B 02 01 8D 82 E7 F8 18 FB 27 F7 40 56 88  B5 46 F8 D0 F6 42 80 11 01 D0 34 D0 00 00 01 01  08 0A A5 07 E4 F5 0A 7F 36 C5,2210037,2,,"alert tcp any any -> any any (msg:""SURICATA STREAM FIN recv but no session""; stream-event:fin_but_no_session; classtype:protocol-command-decode; sid:2210037; rev:2;)"
33 33 00 01 00 02 02 8B  C2 CC 86 87 86 DD 60 0F 13 73 00 40 11 01 FE 80  00 00 00 00 00 00 00 8B C2 FF FE CC 86 87 FF 02  00 00 00 00 00 00 00 00 00 00 00 01 00 02 02 22  02 23 00 40 92 46 01 47 8E E3 00 01 00 0E 00 01  00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06 00 08  00 17 00 18 00 27 00 1F 00 08 00 02 FF FF 00 03  00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,2030387,2,01 47 8E E3 00 01 00 0E  00 01 00 01 2C B2 AC 97 02 8B C2 CC 86 87 00 06  00 08 00 17 00 18 00 27 00 1F 00 08 00 02 FF FF  00 03 00 0C C2 CC 86 87 00 00 0E 10 00 00 15 18,"alert ipv6 any any -> ff00::/8 any (msg:""ET EXPLOIT Possible CVE-2020-11899 Multicast out-of-bound read"";  reference:url,www.jsof-tech.com/ripple20/; classtype:attempted-admin; sid:2030387; rev:2; metadata:created_at 2020_06_22, former_category EXPLOIT, performance_impact Significant, signature_severity Major, updated_at 2020_08_20;)"
```
