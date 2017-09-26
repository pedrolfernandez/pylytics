# pylytics


## Introduction

Pylytics is a project created as data analytics showcase based on Python pandas library.
The idea behind is, given an input CSV file, to generate one or more output reports defined by means of a generic configuration. 
In other terms, creating a generic report generator.

The generic configuration is based on two phases, and each phase enables a set of specific features:
- **Input Processing**
	- Filter the input columns of the CSV to focus only on the columns of interest
	- Alter the input columns (e.g. column in miliseconds to seconds, remove the @domain of a SIP URI, etc)
	- Define new columns (e.g. new column prefix by taking the first digits of a phone number column)
	- Apply filtering (e.g. filter calls only with duration > 0 seconds)
- **Report Generation**. It takes as input the result of the Input Processing phase. After defining a list of keys, we can apply a generic aggregation operation for any column of interest

I explain the above by using an example. Let's suppose we want to process the following CSV file, which contains call detail records (CDRs) extracted from a phone system.

![inputcsv](https://user-images.githubusercontent.com/26331744/30849616-32fa1cd2-a2a3-11e7-8018-2602cc883306.png)

We can define a report to extract the number of calls and total spoken minutes, per minute, for the calls destinated to UK. The output report would look as follows:

![generatedreport](https://user-images.githubusercontent.com/26331744/30849615-32a8a352-a2a3-11e7-818d-6a27f46d9daf.png)

The related config to achieve the above purpose is very straighforward, see below. As we can see many different kind of reports can be defined to reach our analysis goals.

```
# INPUT PROCESSING

[columns]
columns=src_user,dst_user,state_msg,call_time,setup_start_ts

[mappings]
call_time=call_time / 1000
src_user=src_user.split('@')[0]
dst_user=dst_user.split('@')[0]

[newcols]
dst_prefix=dst_user,dst_user[:3]
start_min=setup_start_ts,setup_start_ts[:16]

[filter]
filter=call_time>2

# DATA REPORTS

[datareport1]
name=Calls to UK per minute
filter=dst_prefix=="+44"
keys=start_min
col1_name=Num Calls
col1_col=call_time
col1_op=count
col2_name=Total spoken minutes
col2_col=call_time
col2_op=sum
```

