title: "Flask"
description: "Site now running on Flask and it's faster than ever."
created: 2012-01-26 08:59:59
tags:
  - development
  - design
  - flask
---

This site is now running on Flask.




uWSG


Last login: Thu Jan 26 08:07:05 on ttys001
~$ ab -n 100 -c 2 http://test.jamiecurle.com/blog.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog.html
Document Length:        30446 bytes

Concurrency Level:      2
Time taken for tests:   29.051 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      3060500 bytes
HTML transferred:       3044600 bytes
Requests per second:    3.44 [#/sec] (mean)
Time per request:       581.021 [ms] (mean)
Time per request:       290.511 [ms] (mean, across all concurrent requests)
Transfer rate:          102.88 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:   549  579  17.4    584     616
Waiting:      549  579  17.4    584     616
Total:        549  579  17.4    584     616

Percentage of the requests served within a certain time (ms)
  50%    584
  66%    588
  75%    591
  80%    596
  90%    600
  95%    608
  98%    612
  99%    616
 100%    616 (longest request)
~$ ab -n 100 -c 2 http://127.0.0.1:5000/blog.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)...apr_socket_recv: Connection reset by peer (54)
Total of 34 requests completed
~$ ab -n 10 -c 2  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      2
Time taken for tests:   5.866 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    1.70 [#/sec] (mean)
Time per request:       1173.154 [ms] (mean)
Time per request:       586.577 [ms] (mean, across all concurrent requests)
Transfer rate:          8.56 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:  1150 1172  16.8   1175    1196
Waiting:     1150 1172  16.8   1175    1196
Total:       1150 1173  16.8   1175    1196

Percentage of the requests served within a certain time (ms)
  50%   1175
  66%   1183
  75%   1189
  80%   1191
  90%   1196
  95%   1196
  98%   1196
  99%   1196
 100%   1196 (longest request)
~$ ab -n 10 -c 2  http://127.0.0.1:5000/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      2
Time taken for tests:   11.806 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51400 bytes
HTML transferred:       49850 bytes
Requests per second:    0.85 [#/sec] (mean)
Time per request:       2361.291 [ms] (mean)
Time per request:       1180.646 [ms] (mean, across all concurrent requests)
Transfer rate:          4.25 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:  1203 2250 368.9   2358    2432
Waiting:     1202 2249 369.1   2358    2432
Total:       1203 2250 368.9   2358    2432

Percentage of the requests served within a certain time (ms)
  50%   2358
  66%   2366
  75%   2389
  80%   2390
  90%   2432
  95%   2432
  98%   2432
  99%   2432
 100%   2432 (longest request)
~$ ab -n 10 -c 2  http://dev.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking dev.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        dev.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        168 bytes

Concurrency Level:      2
Time taken for tests:   0.001 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Non-2xx responses:      10
Total transferred:      3170 bytes
HTML transferred:       1680 bytes
Requests per second:    9469.70 [#/sec] (mean)
Time per request:       0.211 [ms] (mean)
Time per request:       0.106 [ms] (mean, across all concurrent requests)
Transfer rate:          2931.54 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    0   0.1      0       0
Waiting:        0    0   0.1      0       0
Total:          0    0   0.1      0       0

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      0
  75%      0
  80%      0
  90%      0
  95%      0
  98%      0
  99%      0
 100%      0 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   10.685 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    0.94 [#/sec] (mean)
Time per request:       1068.499 [ms] (mean)
Time per request:       1068.499 [ms] (mean, across all concurrent requests)
Transfer rate:          4.70 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:  1059 1068  11.5   1063    1092
Waiting:     1059 1068  11.5   1063    1092
Total:       1059 1068  11.5   1063    1092

Percentage of the requests served within a certain time (ms)
  50%   1063
  66%   1068
  75%   1071
  80%   1086
  90%   1092
  95%   1092
  98%   1092
  99%   1092
 100%   1092 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   10.543 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    0.95 [#/sec] (mean)
Time per request:       1054.266 [ms] (mean)
Time per request:       1054.266 [ms] (mean, across all concurrent requests)
Transfer rate:          4.76 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:  1039 1054  12.5   1054    1082
Waiting:     1039 1054  12.5   1054    1082
Total:       1039 1054  12.5   1054    1082

Percentage of the requests served within a certain time (ms)
  50%   1054
  66%   1054
  75%   1054
  80%   1066
  90%   1082
  95%   1082
  98%   1082
  99%   1082
 100%   1082 (longest request)
~$ ab -n 10 -c 1 http://test.jamiecurle.com/about.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /about.html
Document Length:        2096 bytes

Concurrency Level:      1
Time taken for tests:   0.074 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      22540 bytes
HTML transferred:       20960 bytes
Requests per second:    134.38 [#/sec] (mean)
Time per request:       7.442 [ms] (mean)
Time per request:       7.442 [ms] (mean, across all concurrent requests)
Transfer rate:          295.78 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     3    7   6.7      3      19
Waiting:        3    7   6.7      3      19
Total:          3    7   6.7      3      19

Percentage of the requests served within a certain time (ms)
  50%      3
  66%      4
  75%     15
  80%     17
  90%     19
  95%     19
  98%     19
  99%     19
 100%     19 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   10.517 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    0.95 [#/sec] (mean)
Time per request:       1051.677 [ms] (mean)
Time per request:       1051.677 [ms] (mean, across all concurrent requests)
Transfer rate:          4.78 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:  1043 1052   8.2   1053    1066
Waiting:     1043 1052   8.2   1053    1066
Total:       1043 1052   8.2   1053    1066

Percentage of the requests served within a certain time (ms)
  50%   1053
  66%   1057
  75%   1058
  80%   1061
  90%   1066
  95%   1066
  98%   1066
  99%   1066
 100%   1066 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        172 bytes

Concurrency Level:      1
Time taken for tests:   0.002 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Non-2xx responses:      10
Total transferred:      3230 bytes
HTML transferred:       1720 bytes
Requests per second:    6207.32 [#/sec] (mean)
Time per request:       0.161 [ms] (mean)
Time per request:       0.161 [ms] (mean, across all concurrent requests)
Transfer rate:          1957.97 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    0   0.0      0       0
Waiting:        0    0   0.0      0       0
Total:          0    0   0.0      0       0

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      0
  75%      0
  80%      0
  90%      0
  95%      0
  98%      0
  99%      0
 100%      0 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        172 bytes

Concurrency Level:      1
Time taken for tests:   0.002 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Non-2xx responses:      10
Total transferred:      3230 bytes
HTML transferred:       1720 bytes
Requests per second:    5396.65 [#/sec] (mean)
Time per request:       0.185 [ms] (mean)
Time per request:       0.185 [ms] (mean, across all concurrent requests)
Transfer rate:          1702.26 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    0   0.0      0       0
Waiting:        0    0   0.0      0       0
Total:          0    0   0.1      0       0

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      0
  75%      0
  80%      0
  90%      0
  95%      0
  98%      0
  99%      0
 100%      0 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   10.752 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    0.93 [#/sec] (mean)
Time per request:       1075.181 [ms] (mean)
Time per request:       1075.181 [ms] (mean, across all concurrent requests)
Transfer rate:          4.67 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:  1052 1075  16.4   1067    1099
Waiting:     1052 1075  16.4   1067    1099
Total:       1052 1075  16.4   1067    1100

Percentage of the requests served within a certain time (ms)
  50%   1067
  66%   1074
  75%   1094
  80%   1098
  90%   1100
  95%   1100
  98%   1100
  99%   1100
 100%   1100 (longest request)
~$ ab -n 10 -c 1 http://test.jamiecurle.com/about.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /about.html
Document Length:        2096 bytes

Concurrency Level:      1
Time taken for tests:   0.058 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      22540 bytes
HTML transferred:       20960 bytes
Requests per second:    173.17 [#/sec] (mean)
Time per request:       5.775 [ms] (mean)
Time per request:       5.775 [ms] (mean, across all concurrent requests)
Transfer rate:          381.18 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     3    6   4.3      3      17
Waiting:        3    6   4.3      3      17
Total:          3    6   4.3      3      17

Percentage of the requests served within a certain time (ms)
  50%      3
  66%      7
  75%      7
  80%      7
  90%     17
  95%     17
  98%     17
  99%     17
 100%     17 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   10.579 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    0.95 [#/sec] (mean)
Time per request:       1057.876 [ms] (mean)
Time per request:       1057.876 [ms] (mean, across all concurrent requests)
Transfer rate:          4.75 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:  1050 1058   9.6   1054    1077
Waiting:     1050 1058   9.6   1054    1077
Total:       1050 1058   9.6   1054    1077

Percentage of the requests served within a certain time (ms)
  50%   1054
  66%   1058
  75%   1066
  80%   1068
  90%   1077
  95%   1077
  98%   1077
  99%   1077
 100%   1077 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   10.688 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    0.94 [#/sec] (mean)
Time per request:       1068.780 [ms] (mean)
Time per request:       1068.780 [ms] (mean, across all concurrent requests)
Transfer rate:          4.70 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:  1052 1069  10.8   1071    1087
Waiting:     1052 1069  10.8   1071    1087
Total:       1052 1069  10.8   1071    1087

Percentage of the requests served within a certain time (ms)
  50%   1071
  66%   1074
  75%   1076
  80%   1076
  90%   1087
  95%   1087
  98%   1087
  99%   1087
 100%   1087 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   0.184 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    54.36 [#/sec] (mean)
Time per request:       18.397 [ms] (mean)
Time per request:       18.397 [ms] (mean, across all concurrent requests)
Transfer rate:          273.01 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    11   18  11.7     11      36
Waiting:       10   18  11.7     11      36
Total:         11   18  11.7     11      36

Percentage of the requests served within a certain time (ms)
  50%     11
  66%     12
  75%     35
  80%     35
  90%     36
  95%     36
  98%     36
  99%     36
 100%     36 (longest request)
~$ ab -n 10 -c 1 http://127.0.0.1:5000/blog.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog.html
Document Length:        30446 bytes

Concurrency Level:      1
Time taken for tests:   0.082 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      306020 bytes
HTML transferred:       304460 bytes
Requests per second:    122.13 [#/sec] (mean)
Time per request:       8.188 [ms] (mean)
Time per request:       8.188 [ms] (mean, across all concurrent requests)
Transfer rate:          3649.69 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     8    8   0.3      8       9
Waiting:        8    8   0.3      8       8
Total:          8    8   0.3      8       9

Percentage of the requests served within a certain time (ms)
  50%      8
  66%      8
  75%      8
  80%      8
  90%      9
  95%      9
  98%      9
  99%      9
 100%      9 (longest request)
~$ ab -n 10 -c 1 http://127.0.0.1:5000/blog.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog.html
Document Length:        30446 bytes

Concurrency Level:      1
Time taken for tests:   0.083 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      306020 bytes
HTML transferred:       304460 bytes
Requests per second:    120.24 [#/sec] (mean)
Time per request:       8.317 [ms] (mean)
Time per request:       8.317 [ms] (mean, across all concurrent requests)
Transfer rate:          3593.43 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     8    8   0.5      8       9
Waiting:        7    8   0.4      8       9
Total:          8    8   0.5      8       9

Percentage of the requests served within a certain time (ms)
  50%      8
  66%      8
  75%      9
  80%      9
  90%      9
  95%      9
  98%      9
  99%      9
 100%      9 (longest request)
~$ ab -n 100 -c 10 http://127.0.0.1:5000/blog.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog.html
Document Length:        30446 bytes

Concurrency Level:      10
Time taken for tests:   0.816 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      3060200 bytes
HTML transferred:       3044600 bytes
Requests per second:    122.51 [#/sec] (mean)
Time per request:       81.629 [ms] (mean)
Time per request:       8.163 [ms] (mean, across all concurrent requests)
Transfer rate:          3661.07 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     8   78  14.0     79      92
Waiting:        8   78  14.0     79      92
Total:          8   78  14.0     79      92

Percentage of the requests served within a certain time (ms)
  50%     79
  66%     80
  75%     81
  80%     84
  90%     90
  95%     92
  98%     92
  99%     92
 100%     92 (longest request)
~$ ab -n 100 -c 10 http://127.0.0.1:5000/blog.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog.html
Document Length:        30446 bytes

Concurrency Level:      10
Time taken for tests:   0.816 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      3060200 bytes
HTML transferred:       3044600 bytes
Requests per second:    122.55 [#/sec] (mean)
Time per request:       81.600 [ms] (mean)
Time per request:       8.160 [ms] (mean, across all concurrent requests)
Transfer rate:          3662.35 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     8   78  14.1     79      93
Waiting:        8   78  14.0     79      93
Total:          9   78  14.0     79      93

Percentage of the requests served within a certain time (ms)
  50%     79
  66%     80
  75%     81
  80%     84
  90%     92
  95%     93
  98%     93
  99%     93
 100%     93 (longest request)
~$ ab -n 100 -c 10 http://127.0.0.1:5000/about.html
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /about.html
Document Length:        2096 bytes

Concurrency Level:      10
Time taken for tests:   0.075 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      225100 bytes
HTML transferred:       209600 bytes
Requests per second:    1338.10 [#/sec] (mean)
Time per request:       7.473 [ms] (mean)
Time per request:       0.747 [ms] (mean, across all concurrent requests)
Transfer rate:          2941.46 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     1    7   1.2      7       8
Waiting:        1    7   1.2      7       8
Total:          1    7   1.1      7       8

Percentage of the requests served within a certain time (ms)
  50%      7
  66%      8
  75%      8
  80%      8
  90%      8
  95%      8
  98%      8
  99%      8
 100%      8 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   0.142 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    70.35 [#/sec] (mean)
Time per request:       14.216 [ms] (mean)
Time per request:       14.216 [ms] (mean, across all concurrent requests)
Transfer rate:          353.31 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5   14  11.9      5      29
Waiting:        5   14  11.9      5      29
Total:          5   14  11.9      5      29

Percentage of the requests served within a certain time (ms)
  50%      5
  66%     27
  75%     28
  80%     29
  90%     29
  95%     29
  98%     29
  99%     29
 100%     29 (longest request)
~$ ab -n 10 -c 1  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      1
Time taken for tests:   0.075 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      51430 bytes
HTML transferred:       49850 bytes
Requests per second:    132.88 [#/sec] (mean)
Time per request:       7.526 [ms] (mean)
Time per request:       7.526 [ms] (mean, across all concurrent requests)
Transfer rate:          667.37 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5    7   7.7      5      29
Waiting:        5    7   7.7      5      29
Total:          5    7   7.7      5      29

Percentage of the requests served within a certain time (ms)
  50%      5
  66%      5
  75%      5
  80%      6
  90%     29
  95%     29
  98%     29
  99%     29
 100%     29 (longest request)
~$ ab -n 100 -c 10  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      10
Time taken for tests:   0.179 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      514300 bytes
HTML transferred:       498500 bytes
Requests per second:    557.81 [#/sec] (mean)
Time per request:       17.927 [ms] (mean)
Time per request:       1.793 [ms] (mean, across all concurrent requests)
Transfer rate:          2801.56 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       3
Processing:     4   17   9.1     14      42
Waiting:        4   17   9.1     14      42
Total:          5   17   9.1     15      42

Percentage of the requests served within a certain time (ms)
  50%     15
  66%     18
  75%     20
  80%     24
  90%     37
  95%     37
  98%     42
  99%     42
 100%     42 (longest request)
~$ ab -n 100 -c 10  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      10
Time taken for tests:   0.157 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      514300 bytes
HTML transferred:       498500 bytes
Requests per second:    635.38 [#/sec] (mean)
Time per request:       15.739 [ms] (mean)
Time per request:       1.574 [ms] (mean, across all concurrent requests)
Transfer rate:          3191.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.2      0       8
Processing:     5   15   7.6     13      46
Waiting:        5   15   7.6     13      46
Total:          5   15   7.8     14      46

Percentage of the requests served within a certain time (ms)
  50%     14
  66%     16
  75%     18
  80%     19
  90%     24
  95%     33
  98%     46
  99%     46
 100%     46 (longest request)
~$ ab -n 100 -c 10  http://test.jamiecurle.com/blog/_test/ 
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/_test/
Document Length:        4985 bytes

Concurrency Level:      10
Time taken for tests:   0.156 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      514300 bytes
HTML transferred:       498500 bytes
Requests per second:    641.10 [#/sec] (mean)
Time per request:       15.598 [ms] (mean)
Time per request:       1.560 [ms] (mean, across all concurrent requests)
Transfer rate:          3219.92 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       2
Processing:     4   15   5.8     14      36
Waiting:        4   15   5.8     13      36
Total:          5   15   5.8     14      36

Percentage of the requests served within a certain time (ms)
  50%     14
  66%     16
  75%     18
  80%     19
  90%     22
  95%     27
  98%     32
  99%     36
 100%     36 (longest request)
~$ ab -n 100 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   0.384 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      595000 bytes
HTML transferred:       579500 bytes
Requests per second:    260.40 [#/sec] (mean)
Time per request:       38.402 [ms] (mean)
Time per request:       3.840 [ms] (mean, across all concurrent requests)
Transfer rate:          1513.08 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5   37   5.8     38      42
Waiting:        5   36   5.8     38      42
Total:          5   37   5.8     38      42

Percentage of the requests served within a certain time (ms)
  50%     38
  66%     38
  75%     38
  80%     38
  90%     39
  95%     40
  98%     41
  99%     42
 100%     42 (longest request)
~$ ab -n 100 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   0.394 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      595000 bytes
HTML transferred:       579500 bytes
Requests per second:    253.66 [#/sec] (mean)
Time per request:       39.423 [ms] (mean)
Time per request:       3.942 [ms] (mean, across all concurrent requests)
Transfer rate:          1473.90 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     5   38   6.3     39      44
Waiting:        4   37   6.3     38      44
Total:          5   38   6.3     39      44

Percentage of the requests served within a certain time (ms)
  50%     39
  66%     39
  75%     40
  80%     40
  90%     41
  95%     43
  98%     44
  99%     44
 100%     44 (longest request)
~$ ab -n 100 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   0.446 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      595000 bytes
HTML transferred:       579500 bytes
Requests per second:    224.25 [#/sec] (mean)
Time per request:       44.594 [ms] (mean)
Time per request:       4.459 [ms] (mean, across all concurrent requests)
Transfer rate:          1302.99 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    25   43   4.3     42      64
Waiting:       24   42   4.3     42      64
Total:         25   43   4.3     42      64

Percentage of the requests served within a certain time (ms)
  50%     42
  66%     42
  75%     43
  80%     44
  90%     47
  95%     49
  98%     60
  99%     64
 100%     64 (longest request)
~$ ab -n 100 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   0.418 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      595000 bytes
HTML transferred:       579500 bytes
Requests per second:    239.28 [#/sec] (mean)
Time per request:       41.792 [ms] (mean)
Time per request:       4.179 [ms] (mean, across all concurrent requests)
Transfer rate:          1390.36 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4   40   6.7     42      43
Waiting:        4   40   6.7     41      43
Total:          5   40   6.6     42      43

Percentage of the requests served within a certain time (ms)
  50%     42
  66%     42
  75%     42
  80%     42
  90%     42
  95%     42
  98%     43
  99%     43
 100%     43 (longest request)
~$ ab -n 100 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   0.423 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      595000 bytes
HTML transferred:       579500 bytes
Requests per second:    236.45 [#/sec] (mean)
Time per request:       42.292 [ms] (mean)
Time per request:       4.229 [ms] (mean, across all concurrent requests)
Transfer rate:          1373.92 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5   40   7.2     41      49
Waiting:        4   40   7.2     41      49
Total:          5   40   7.1     41      49

Percentage of the requests served within a certain time (ms)
  50%     41
  66%     42
  75%     42
  80%     43
  90%     46
  95%     48
  98%     49
  99%     49
 100%     49 (longest request)
~$ ab -n 100 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   0.429 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      595000 bytes
HTML transferred:       579500 bytes
Requests per second:    233.01 [#/sec] (mean)
Time per request:       42.917 [ms] (mean)
Time per request:       4.292 [ms] (mean, across all concurrent requests)
Transfer rate:          1353.89 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4   41   7.2     42      49
Waiting:        4   41   7.2     42      48
Total:          5   41   7.1     42      49

Percentage of the requests served within a certain time (ms)
  50%     42
  66%     42
  75%     43
  80%     44
  90%     46
  95%     48
  98%     48
  99%     49
 100%     49 (longest request)
~$ ab -n 100 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   0.417 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      595000 bytes
HTML transferred:       579500 bytes
Requests per second:    239.81 [#/sec] (mean)
Time per request:       41.701 [ms] (mean)
Time per request:       4.170 [ms] (mean, across all concurrent requests)
Transfer rate:          1393.40 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5   40   6.6     41      43
Waiting:        5   40   6.6     41      43
Total:          5   40   6.6     41      43

Percentage of the requests served within a certain time (ms)
  50%     41
  66%     42
  75%     42
  80%     42
  90%     42
  95%     43
  98%     43
  99%     43
 100%     43 (longest request)
~$ ab -n 100 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   0.422 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      595000 bytes
HTML transferred:       579500 bytes
Requests per second:    237.23 [#/sec] (mean)
Time per request:       42.153 [ms] (mean)
Time per request:       4.215 [ms] (mean, across all concurrent requests)
Transfer rate:          1378.45 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4   40   6.8     41      48
Waiting:        4   40   6.8     41      48
Total:          5   40   6.8     41      49

Percentage of the requests served within a certain time (ms)
  50%     41
  66%     42
  75%     42
  80%     42
  90%     42
  95%     48
  98%     48
  99%     49
 100%     49 (longest request)
~$ ab -n 1000 -c 10  http://127.0.0.1:5000/blog/handstands/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/handstands/
Document Length:        5795 bytes

Concurrency Level:      10
Time taken for tests:   4.208 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Total transferred:      5950000 bytes
HTML transferred:       5795000 bytes
Requests per second:    237.62 [#/sec] (mean)
Time per request:       42.085 [ms] (mean)
Time per request:       4.208 [ms] (mean, across all concurrent requests)
Transfer rate:          1380.67 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     5   42   2.6     42      49
Waiting:        5   42   2.6     42      49
Total:          5   42   2.6     42      49

Percentage of the requests served within a certain time (ms)
  50%     42
  66%     42
  75%     42
  80%     42
  90%     43
  95%     45
  98%     48
  99%     49
 100%     49 (longest request)
~$ ab -n 1000 -c 10  http://127.0.0.1:5000/blog/_test
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/_test
Document Length:        275 bytes

Concurrency Level:      10
Time taken for tests:   0.799 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Non-2xx responses:      1000
Total transferred:      490000 bytes
HTML transferred:       275000 bytes
Requests per second:    1252.32 [#/sec] (mean)
Time per request:       7.985 [ms] (mean)
Time per request:       0.799 [ms] (mean, across all concurrent requests)
Transfer rate:          599.26 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       1
Processing:     1    8   1.1      8      16
Waiting:        1    8   1.1      7      15
Total:          2    8   1.1      8      16

Percentage of the requests served within a certain time (ms)
  50%      8
  66%      8
  75%      8
  80%      8
  90%      9
  95%     10
  98%     12
  99%     13
 100%     16 (longest request)
~$ ab -n 1000 -c 10  http://127.0.0.1:5000/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Werkzeug/0.8.2
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /blog/tough-mudder-training/
Document Length:        10791 bytes

Concurrency Level:      10
Time taken for tests:   4.063 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Total transferred:      10947000 bytes
HTML transferred:       10791000 bytes
Requests per second:    246.14 [#/sec] (mean)
Time per request:       40.627 [ms] (mean)
Time per request:       4.063 [ms] (mean, across all concurrent requests)
Transfer rate:          2631.34 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     4   40   2.8     40      53
Waiting:        4   40   2.8     40      53
Total:          5   40   2.8     40      53

Percentage of the requests served within a certain time (ms)
  50%     40
  66%     40
  75%     41
  80%     41
  90%     42
  95%     44
  98%     47
  99%     49
 100%     53 (longest request)
~$ ab -n 1000 -c 10  http://test.jamiecurle.com/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/tough-mudder-training/
Document Length:        10791 bytes

Concurrency Level:      10
Time taken for tests:   1.802 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Total transferred:      10950000 bytes
HTML transferred:       10791000 bytes
Requests per second:    555.06 [#/sec] (mean)
Time per request:       18.016 [ms] (mean)
Time per request:       1.802 [ms] (mean, across all concurrent requests)
Transfer rate:          5935.51 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.7      0       5
Processing:     5   18  11.1     15      91
Waiting:        5   17  11.0     14      90
Total:          5   18  11.0     15      91

Percentage of the requests served within a certain time (ms)
  50%     15
  66%     18
  75%     21
  80%     22
  90%     30
  95%     38
  98%     53
  99%     73
 100%     91 (longest request)
~$ ab -n 1000 -c 10  http://test.jamiecure.com/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecure.com (be patient)
apr_sockaddr_info_get() for test.jamiecure.com: nodename nor servname provided, or not known (670008)
~$ ab -n 1000 -c 10  http://test.jamiecurle.com/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/tough-mudder-training/
Document Length:        10791 bytes

Concurrency Level:      10
Time taken for tests:   1.742 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Total transferred:      10950000 bytes
HTML transferred:       10791000 bytes
Requests per second:    573.96 [#/sec] (mean)
Time per request:       17.423 [ms] (mean)
Time per request:       1.742 [ms] (mean, across all concurrent requests)
Transfer rate:          6137.55 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.8      0      10
Processing:     5   17   9.0     15      72
Waiting:        4   17   8.9     14      72
Total:          5   17   9.0     15      72

Percentage of the requests served within a certain time (ms)
  50%     15
  66%     18
  75%     20
  80%     23
  90%     28
  95%     35
  98%     45
  99%     51
 100%     72 (longest request)
~$ ab -n 1000 -c 10  http://jamiecurle.com/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking jamiecurle.com (be patient)
Completed 100 requests
^C

Server Software:        nginx/0.8.53
Server Hostname:        jamiecurle.com
Server Port:            80

Document Path:          /blog/tough-mudder-training/
Document Length:        11530 bytes

Concurrency Level:      10
Time taken for tests:   5.288 seconds
Complete requests:      102
Failed requests:        0
Write errors:           0
Total transferred:      1210286 bytes
HTML transferred:       1194280 bytes
Requests per second:    19.29 [#/sec] (mean)
Time per request:       518.479 [ms] (mean)
Time per request:       51.848 [ms] (mean, across all concurrent requests)
Transfer rate:          223.49 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      145  152   5.0    151     172
Processing:   307  338  52.3    318     518
Waiting:      153  178  47.6    161     330
Total:        453  491  54.0    470     677

Percentage of the requests served within a certain time (ms)
  50%    470
  66%    476
  75%    482
  80%    491
  90%    573
  95%    641
  98%    652
  99%    660
 100%    677 (longest request)
~$ ab -n 10 -c 2  http://jamiecurle.com/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking jamiecurle.com (be patient).....done


Server Software:        nginx/0.8.53
Server Hostname:        jamiecurle.com
Server Port:            80

Document Path:          /blog/tough-mudder-training/
Document Length:        11530 bytes

Concurrency Level:      2
Time taken for tests:   2.315 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      116810 bytes
HTML transferred:       115300 bytes
Requests per second:    4.32 [#/sec] (mean)
Time per request:       463.022 [ms] (mean)
Time per request:       231.511 [ms] (mean, across all concurrent requests)
Transfer rate:          49.27 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:      144  150   7.7    148     171
Processing:   306  313   5.4    312     325
Waiting:      153  158   4.9    156     169
Total:        454  463   8.5    461     481

Percentage of the requests served within a certain time (ms)
  50%    461
  66%    462
  75%    468
  80%    471
  90%    481
  95%    481
  98%    481
  99%    481
 100%    481 (longest request)
~$ ab -n 10 -c 2  http://test.jamiecurle.com/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/tough-mudder-training/
Document Length:        10791 bytes

Concurrency Level:      2
Time taken for tests:   0.030 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      109500 bytes
HTML transferred:       107910 bytes
Requests per second:    329.47 [#/sec] (mean)
Time per request:       6.070 [ms] (mean)
Time per request:       3.035 [ms] (mean, across all concurrent requests)
Transfer rate:          3523.12 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.2      6       6
Waiting:        6    6   0.2      6       6
Total:          6    6   0.2      6       6

Percentage of the requests served within a certain time (ms)
  50%      6
  66%      6
  75%      6
  80%      6
  90%      6
  95%      6
  98%      6
  99%      6
 100%      6 (longest request)
~$ ab -n 10 -c 2  http://test.jamiecurle.com/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient).....done


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/tough-mudder-training/
Document Length:        10791 bytes

Concurrency Level:      2
Time taken for tests:   0.030 seconds
Complete requests:      10
Failed requests:        0
Write errors:           0
Total transferred:      109500 bytes
HTML transferred:       107910 bytes
Requests per second:    329.14 [#/sec] (mean)
Time per request:       6.076 [ms] (mean)
Time per request:       3.038 [ms] (mean, across all concurrent requests)
Transfer rate:          3519.64 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    6   0.5      6       7
Waiting:        5    6   0.5      6       7
Total:          6    6   0.5      6       7

Percentage of the requests served within a certain time (ms)
  50%      6
  66%      6
  75%      6
  80%      7
  90%      7
  95%      7
  98%      7
  99%      7
 100%      7 (longest request)
~$ ab -n 1000 -c 100  http://test.jamiecurle.com/blog/tough-mudder-training/
This is ApacheBench, Version 2.3 <$Revision: 1178079 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking test.jamiecurle.com (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        nginx/1.0.4
Server Hostname:        test.jamiecurle.com
Server Port:            80

Document Path:          /blog/tough-mudder-training/
Document Length:        10791 bytes

Concurrency Level:      100
Time taken for tests:   1.766 seconds
Complete requests:      1000
Failed requests:        0
Write errors:           0
Total transferred:      10950000 bytes
HTML transferred:       10791000 bytes
Requests per second:    566.38 [#/sec] (mean)
Time per request:       176.561 [ms] (mean)
Time per request:       1.766 [ms] (mean, across all concurrent requests)
Transfer rate:          6056.46 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.9      0       5
Processing:    28  168  23.6    170     255
Waiting:       28  168  23.7    169     255
Total:         31  169  23.4    170     256

Percentage of the requests served within a certain time (ms)
  50%    170
  66%    174
  75%    177
  80%    180
  90%    189
  95%    197
  98%    206
  99%    214
 100%    256 (longest request)
~$ 
