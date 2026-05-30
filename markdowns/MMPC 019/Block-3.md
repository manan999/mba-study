Indira Gandhi
National Open University
School of Management Studies

MMPC-019
TOTAL QUALITY
MANAGEMENT

Quality-Strategic
Planning

Block

3

TOOLS  AND TECHNIQUES

UNIT 7
Statistical Quality Control

UNIT 8
Tools and Techniques of TQM

155

177

Strategic Perspectives

BLOCK 3 TOOLS &TECHNIQUES

This  block  has  the  following  two  units  and  presents  basic  tools,  techniques
and concepts useful for developing and implementing a TQM programme. In
addition to statistical quality control (SQC), Pareto Analysis and Six Sigma, several
other concepts, tools and techniques e.g. Quality Circles, Benchmarking, Quality
Function Deployment, Reengineering, Zero Defects etc. are also discussed.

Unit 7

Unit 8

Statistical Quality Control

Tools and Techniques of TQM

154

UNIT 7 STATISTICAL QUALITY CONTROL

Statistical Quality
Control

Objectives

After reading this unit you should be able to:

• Understand the use of statistical thinking to quality improvement;

• Use seven tools to troubleshoot quality problems;

• Determine process capability of a manufacturing process;

• Explain the concept of a control chart;

• Understand the principles behind sampling methods.

Structure

7.1

Introduction to Statistical Quality Control

7.2 Process Capability

7.3 Seven Quality Improvement Tools

7.4 Control Charts

7.5 Control Charts for Attributes

7.6 Choosing the Correct SPC Chart

7.7 Acceptance Sampling

7.8 Summary

7.9 Key Words

7.10 Self-Assessment Questions

7.11 Further Readings

7.1

INTRODUCTION  TO  STATISTICAL  QUALITY
CONTROL

The concept of TQM is basically very simple. Each part of the organization has
customers,  some  external  and  many  internal.  Identifying  what  the  customer
requirements  are  and  setting  about  to  meet  them  is  the  core  of  a  total  quality
approach. This requires a good management system, methods including Statistical
Quality Control (SQC), and teamwork.

A  well-operated,  documented  management  system  provides  the  necessary
foundation for the successful application of SQC. Note, however, that SQC is not
just a collection of techniques. It is a strategy for reducing variability, the root
cause of many quality problems. SQC refers to the use of statistical methods to
improve or enhance quality for customer satisfaction. However, this task is seldom
trivial because real-world processes are affected by numerous uncontrolled factors.
For instance, within every factory, conditions fluctuate with time. Variations occur
in  the  incoming  materials,  in  machine  conditions,  in  the  environment,  and  in

155

Tools and Techniques

156

operator performance. A steel plant, for example, may purchase good quality ore
from a mine, but the physical and chemical characteristics of ore coming from
different locations in the mine may vary. Thus, everything isn’t always “in control.”

For e.g. in welding, it is not possible to form two exactly identical joints, and
faulty joints may occur occasionally. In a cutting process, the size of each piece
of  material  cut  varies;  even  the  most  high-quality  cutting  machine  has  some
inherent variability. In addition to such inherent variability, a large number of
other factors may also influence processes. Many of these variations cannot be
predicted with certainty, although sometimes it is possible to trace the unusual
patterns of such variations to their root cause(s). If we have collected sufficient
data from these variations, we can tell, in terms of probability, what is most likely
to occur next if no action is taken. It we know what is likely to occur the next
given certain conditions, we can take suitable actions to try to maintain or improve
the acceptability of the output. This is the rationale of statistical quality control.

Another prospect in which statistical methods can help to improve product quality
is the design of products and processes. It is now well-understood that over 2/3rd
of all product malfunctions may be traced to their design. Indeed, the characteristics
or quality of a product depends greatly on the choice of materials, settings of
various parameters in the design of the product and the production process settings.
In order to locate an optimal setting of the various parameters which gives the
best product, we may consider using models governing the outcome and the various
parameters, if such models can be established by theory or through experimental
work.

The following two examples illustrate such cases.

Example  1:  In  the  bakery  industry,  the  taste,  tenderness,  and  texture  of  a
kind of bread depend on various input parameters, such as the origin of the
flour  used,  the  amount  of  sugar,  the  amount  of  baking  powder,  the  baking
temperature profile and baking time, and the type of oven used. To improve
the quality of the bread produced, the baker may use a model that relates the
input parameters and the output quality of the bread. It is a formidable task to
find theoretical models quantifying the taste, tenderness, and texture of the
bread produced and relates these quantities to the various input parameters
based on our present scientific knowledge. However, the baker can easily use
statistical methods in regression analysis to establish empirical models and
use them to locate an optimal setting of the input parameters.

Example 2: Sometimes there are great difficulties in solving an engineering
problem using established theoretical models. The heat accumulated on a chip
in an electronic circuit during normal operation will raise the temperature of
the chip and shorten its life. To improve the quality of the circuit, the designer
would like to optimize the design of the circuit so that the heat accumulated
on  the  chip  will  not  exceed  a  certain  level. This  heat  accumulated  can  be
expressed  theoretically  in  terms  of  other  parameters  in  the  circuit  using  a
complicated system of ten or more daunting partial differential equations. It
is  usually  not  possible  to  solve  such  a  system  analytically,  and  to  solve  it
numerically using the computer also has computational difficulties. In this
situation, a statistical methodology known as design of experiments (DOE)

can be used to find an optimal design of the circuit without going through the
complicated method of solving partial differential equations.

Statistical Quality
Control

In other cases, control may need to be exercised online while the process is in
progress based on how the process is performing to maintain product quality.
Thus, in statistical quality control, problems are numerous and diverse.

SQC engages the following three methodologies:

Acceptance Sampling

This  method  is  also  called  “sampling  inspection.”  When  products  require
inspection but it is not feasible to inspect 100% of the products, samples of
the  product  may  be  taken  for  inspection,  and  conclusions  drawn  using  the
results of inspecting the samples. This technique specifies how to draw samples
from a population and what rules to use to determine the acceptability of the
product being inspected.

Statistical Process Control (SPC)

Even in an apparently stable production process, products produced are subject
to random variations. SPC aims at controlling the variability of process output
using  a  device  called  the  control  chart.  On  a  control  chart,  a  certain
characteristic of the product is plotted. Under normal conditions, these plotted
points are expected to vary in a “usual way” on the chart. When abnormal
points  or  patterns  appear  on  the  chart,  it  is  a  statistical  indication  that  the
process parameters or production conditions might have changed undesirably.
At  this  point,  an  investigation  is  conducted  to  discover  unusual  abnormal
conditions  (e.g.,  tool  breakdown,  use  of  wrong  raw  material,  temperature
controller failure, etc.). Subsequently, corrective actions are taken to remove
the abnormality. In addition to the use of control charts, SPC also monitors
process capability as an indicator of the adequacy of the manufacturing process
to  meet  customer  requirements  under  routine  operating  conditions.  In
summary, SPC aims to maintain a stable, capable, and predictable process.

Note,  however,  that  since  SPC  requires  processes  to  display  measurable
variation, it is ineffective for quality levels approaching six-sigma, though it
is quite effective for companies in the early stages of quality improvement
efforts.

Design of Experiments

Trial and error can be used to run experiments in the design of products and
the design of processes in order to find an optimal setting of the parameters
so  that  products  of  good  quality  will  be  produced.  However,  performing
experiments by trial and error unscientifically is frequently very inefficient
in the search for an optimal solution. Application of the statistical methodology
of “design of experiments” (DOE) can help us in performing such experiments
scientifically and systematically. Additionally, such methods greatly reduce
the total effort used in product or process development experiments, increasing
at the same time the accuracy of the results. DOE forms an integral part of
Taguchi  methods,  techniques  that  produce  high-quality  and  robust  product
and process designs.

157

Tools and Techniques

The Correct Use of Statistical Quality Control Methods

The production of a product typically progresses as indicated in the simplified
flow diagram shown in Figure 7.1. In order to improve the quality of the tonal
product, design of experiments (DOE) may be used in Step 1 and Step 2, acceptance
sampling may be used in Step 3 and Step 5, and statistical process control(SPC)
may be used in Step 4.

Figure 7.3: Production from Design to Dispatch

There are several benefits that the SPC approach brings which are as follows:

• There are no restrictions as to the type of the process being controlled or

studied, but the process tackled will be improved.

• Decisions guided by SPC are based on facts not opinions. Thus a lot of

emotion is removed from problems by SPC.

• Quality awareness of the workforce increases because they become directly

involved in the improvement process.

• Knowledge and experience of those who operate the process are released
in a systematic way through the investigative approach. They understand
their  role  in  problem  solving,  which  includes  collecting  facts,
communicating fads, and making decisions.

• Management and supervisors solve problems methodically, instead of by

using a seat-of-the-pants style.

7.2 PROCESS CAPABILITY

We  introduce  now  an  important  concept  employed  in  thinking  statistically
about real life processes. Process capability is the range over which the “natural
variation  “of  a  process  occurs  as  determined  by  the  system  of  common  or
random  causes;  that  is,  process  capability  indicates  what  the  process  can
deliver under “stable “conditions when it is said to be under statistical control.

The  capability  of  a  process  is  the  fraction  of  output  that  can  be  routinely
found to be within specifications (specs). A capable process has 99.73% or
more of its output within specifications.

Process  capability  refers  to  a  process’s  ability  to  produce  parts  within  the
range of engineering or customer specifications. Process control, on the other
hand, refers to maintaining a process’s performance at its current capability
level. This involves activities such as sampling the process product, charting
its  performance,  determining  causes  of  excessive  variation,  and  taking
corrective action.

158

The  capability  of  a  process  is  an  expression  of  how  well  the  process  can
deliver  output  within  the  specifications  compared  to  the  range  of  natural
variability seen in the process. Essentially, process capability expresses the
proportion or fractional output that a process can routinely deliver within the
specifications. By subjecting a process to a capability study, manufacturing
and quality managers can determine whether the process needs improvement
and to what extent.

Knowing process capability allows managers to quantitatively predict how
well a process will meet specifications and specify the equipment requirements
necessary  to  maintain  its  capability.  For  example,  if  a  design  specification
requires metal tubing to be cut within one-tenth of an inch, a process consisting
of a worker using a ruler and hacksaw will likely result in a large percentage
of nonconforming product due to the high inherent or natural variability of
the process. In such a case, the firm has three possible choices: (1) measure
each piece and cut non-conforming tubing, (2) invest in new technology to
develop a better process, or (3) change the specification.

Ultimately, such decisions are usually based on economics. It is important to
note that the cost to produce one unit of a product remains the same under
routine production, whether the product ultimately fails within or outside the
specifications. As such, the firm may be forced to raise the market price of
within-spec products, which may weaken its competitive position. Scrap and
rework of nonconforming parts are therefore poor business strategies, as labour
and  materials  have  already  been  invested  in  producing  the  unacceptable
product. Inspection errors may also allow some nonconforming products to
leave the production facility if the firm aims to make parts that just meet the
specifications. However, investing in new technology may require substantial
investment that the firm cannot afford.

Changes  in  design,  on  the  other  hand,  may  sacrifice  fitness-for-use
requirements  and  result  in  a  lower  quality  product.  Thus,  these  factors
demonstrate  the  need  to  consider  process  capability  during  product  design
and  in  the  acceptance  of  new  contracts.  Many  firms  now  require  process
capability  data  from  their  vendors.  Both  ISO  9000  and  QS  9000  quality
management systems require a firm to determine its process capability.

Process  capability  has  three  important  components:  (1)  the  design
specifications, (2) the centering of the natural variation, and (3) the range or
spread of variation. If the process is in control but cannot produce according
to  the  design  specifications,  the  question  should  be  raised  whether  the
specifications have been correctly applied or if they may be relaxed without
adversely  affecting  the  assembly  or  subsequent  use  of  the  product.  If  the
specifications are realistic and firm, an effort must be made to improve the
process  to  the  point  where  it  is  capable  of  producing  consistently  within
specifimcations.

Usually, this can be corrected by a simple adjustment of a machine setting or
recalibrating the inspection equipment used to capture the measurements. If
no action is taken, however, a substantial portion of output will fall outside

Statistical Quality
Control

159

Tools and Techniques

the spec limits even though the process has the inherent capability to meet
specifications.

We may define the study of process capability from another perspective. A
capability study is a technique for analysing the random variability found in
a production process. In every manufacturing process, there is some variability.
This  variability  may  be  large  or  small,  but  it  is  always  present.  It  can  be
divided into two types:

• Variability due to common (random) causes

• Variability due to assignable (special) causes

The first type of variability is said to be inherent in the process, and it can be
expected to occur naturally within a process. It is attributed to a multitude of
factors that behave like a constant system of changes affecting the process called
common or random causes, Such factors include equipment vibration, passing
traffic, atmospheric pressure or temperature changes, electrical voltage or humidity
fluctuations, changes in the operator’s physical or emotional conditions, etc. Such
forces determine whether a coin when tossed will end up showing a head or tail
when  on  the  floor.  Together,  however,  these  “chances”  form  a  unique,  stable
distribution.

Inherent  variability  may  be  reduced  by  changing  the  environment  or  the
technology, but given a set of operating conditions, this variability can never be
completely eliminated from a process. Variability due to assignable causes, on
the other hand, refers to the variation that can be linked to specific or special
causes that disturb a process. Examples are tool failure, power supply interruption,
process controller malfunction, adding wrong ingredients or wrong quantities,
switching a vendor, etc.

Assignable  causes  are  fewer  in  number  and  are  usually  identifiable  through
investigation on the shop floor or an examination of process logs. The effect (i.e.,
the variation in the process) caused by an assignable factor, however, is usually
large  and  detectable  when  compared  with  the  inherent  variability  seen  in  the
process.  If  the  assignable  causes  are  controlled  properly,  the  total  process
variability associated with them can be reduced and even eliminated.

A capability study measures the inherent variability or the performance potential
of a process when no assignable causes are present (i.e., when the process is said
to be in statistical control). Since inherent variability can be described by a unique
distribution, usually a normal distribution, capability can be evaluated by utilizing
the properties of this distribution. Recall that capability is the proportion of routine
process output that remains within product specs.

Even  approximate  capability  calculations  done  using  histograms  enable
manufacturers to take a preventive approach to defects. This approach is in contrast
with  the  traditional  two-step  process:  production  personnel  make  the  product
while  QC  personnel  inspects  and  screen  out  products  that  do  not  meet
specifications. Such QC is wasteful and expensive since it allows plant resources
including time and materials to be put into products that are not saleable. It is also
unreliable  since  even  100  percent  inspection  would  fail  to  catch  all  defective

160

products. SPC aims to correct undesirable changes in the output of a process.
Such changes may affect the centering (or accuracy) of the process, or its variability
(spread or precision).

Statistical Quality
Control

Control Limits are not an Indication of Capability

Those who are new to SPC often have the misconception that they don’t need
to calculate capability indices. Some even think that they can compare their
control limits to the spec limits. This is not true because control limits look at
the distribution of averages while capability indices look at the distribution
of  individual  measurements.  The  statistical  theory  of  the  “central  limit
theorem”  says  that  the  averages  of  samples  or  subgroups  follow  a  normal
distribution more closely. This is why we can easily construct control charts
on process data that are not normally distributed themselves. But averages
cannot  be  used  for  capability  calculation  because  capability  evaluates
individual  parts  delivered  by  a  process.  After  all,  parts  get  shipped  to
customers, not averages.

What Capability Studies Do for You

Capability studies are most often used to quickly determine whether a process
can meet specs or how many parts will exceed the specifications. However, there
are numerous other practical uses:

•

•

•

Estimating the percentage of defective parts to be expected

Evaluating new equipment purchases

Predicting whether design tolerances can be met

• Assigning equipment to production

•

Planning process control checks

• Analyzing the interrelationship of sequential processes

• Making adjustments during manufacture

•

Setting specifications

• Costing out contracts

•

Statistical Quality Control

Since a capability study determines the inherent reproducibility of parts created
in  a  process,  it  can  even  be  applied  to  many  problems  outside  the  domain  of
manufacturing, such as inspection, administration, and engineering.

There are instances where capability measurements are valuable even when it is
not practical to determine in advance if the process is in control. Such an analysis
is called a performance study. Performance studies can be useful for examining
incoming lots of materials or one-time-only production runs. In the case of an
incoming lot, a performance study cannot tell us that the process that produced
the materials is in control, but it may tell us, by the shape of the distribution, what
percent of the parts are out of specs or, more importantly, whether the distribution
was truncated by the vendor sorting out the obvious bad parts.

161

Tools and Techniques

How to Set Up a Capability Study

Before setting up a capability study, we must select the critical dimension or
quality characteristic (it must be a measurable variable) to be examined. This
dimension is the one that must meet product specs. In the simplest case, the
study  dimension  is  the  result  of  a  single,  direct  product  and  measurement
process. In more complicated studies, the critical dimension may be the result
of several processing steps or stages. It may become necessary in these cases
to perform capability studies on each process stage. Studies on early process
stages frequently prove to be more valuable than elaborate capability studies
done on later processes since early processes lay the foundation (i.e., constitute
the input) that may affect later operations.

Once the critical dimensions are selected, data measurements can be collected.
This can be accomplished manually or by using automatic gauging and filtering
linked  to  a  data  collection  device  or  computer.  When  measurements  on  a
critical  dimension  are  made,  it  is  important  to  ensure  that  the  measuring
instrument is as precise as possible, preferably one order of magnitude finer
than the specification. Otherwise, the measuring process itself will contribute
excess  variation  to  the  dimension  data  as  recorded.  Using  handheld  data
collectors with automatic gauges may help reduce errors introduced by the
process of measurement, data recording, and transcription for post-processing
by computer.

The deal situation for data collection is to collect as much data as possible
over a defined time period. This will yield reliable capability number since it
is based upon a large sample size. In the practice of process improvement,
determining process capability is Step 5.

Capability Calculations condition 1: The Process Must be in Control

Process  capability  formulas  commonly  used  by  industry  require  that  the
process must be in control and normally distributed before one takes samples
to estimate process capability. All standard capability indices assume that the
process is in control and the individual data follow a normal distribution. If
the  process  is  not  in  control,  capability  indices  are  not  valid,  even  if  they
appear to indicate the process is capable.

Three  different  statistical  tools  are  used  together  to  determine  whether  a
process is in control and follows a normal distribution. These are

• Control chart

• Visual analysis of a histogram

• Mathematical  analysis  of  the  distribution  to  test  that  the  distribution  is

normal.

162

Note that no single tool can do the job here and all three must be used together.
Control charts are the most common method for maintaining a process in statistical
control. For a process to be in control, all points plotted, on the control chart must
be inside the control limits with no apparent patterns (e.g., trends) be present. A
histogram (allows us to quickly see (a) if any parts are outside the spec limits and
(b) what the distribution’s position is relative to the specification range. If the
process is one that is naturally a normal distribution, then the histogram should
approximate a bell-shaped curve if the process is in control. However, note that a
process  can  be  in  control  but  not  have  its  -  individuals  following  a  normal
distribution if the process is inherently non-normal.

Capability Calculations condition 2: The Process Must be Inherently Normal

Many processes naturally follow a bell-shaped curve (a normal distribution) but
some do not. Examples of non-normal dimensions are round, square, flat and
positional tolerances; they have a natural barrier at zero. In these cases, a perfect
measurement is zero.

There can never be a value less than zero. The standard capability indices are not
valid for such non-normal distributions. Tests for normality are available in SPC
text books that can assist you to identify whether or not a process is normal. If a
process is not normal, you may have to use special capability measures that apply
to non-normal distributions.

Statistical Process Control (SPC) Methodology

Control charts, like the other basic tools for quality improvement, are relatively
simple  to  use.  In  general,  control  charts  have  two  objectives,  (a)  help  restore
accuracy of the process so that the process average stays near the target, and (b)
help minimize variation in the process to ensure that good precision is maintained
in the output .

Control charts have three basic applications: (1) to establish a state of statistical
control, (2) to monitor a process and signal when the process goes out of control,
and (3) to determine process capability. The following is a summary of the steps
required to develop and use control charts. Steps 1 through 4 focus on establishing
a state of statistical control; in step 5, the charts are used for on-going monitoring;
and finally in step 6, the data are used for process capability analysis.

1. Preparation

a. Choose the variable or attribute to be measured

b. Determine the basis, size and frequency of sampling.

c. Set up the correct control chart.

2. Data Collection

a. Record the data

b. Calculate relevant statistics:

c. Plot the statistics on the chart.

Statistical Quality
Control

163

Tools and Techniques

3. Determination of trial control limits.

a. Draw the center line (process average) on the chart.

b. Compute the upper and lower control limits.

4. Analysis and interpretation

a.

Investigate the chart for lack of control

b. Eliminate out-of-control points.

c. Re-compute control limits if necessary.

5. Use as a problem-solving tool

a. Continue data collection and plotting.

b.

Identify out-of-control situations and take corrective action.

6. Use the control chart data to determine process capability, if desired.

7.3 SEVEN QUALITY IMPROVEMENT TOOLS

In  SPC,  numbers  and  information  form  the  basis  for  decisions  and  actions.
Therefore, a thorough data recording system bimanual or otherwise would be an
essential  enabler  for  SPC.  In  order  to  allow  one  to  interpret  fully  and  derive
maximum use of quality-related data, over the past fifty years a set of simple
statistical’ tools’ have evolved. These tools offer any organization an easy means
to collect, present and analyse most of such data. In this section we briefly review
these tools.

In the 1950’s  Japanese industry began to learn and apply statistical methods in
earnestness, methods that American statisticians Walter Shewhart and W Edward
Deming developed in the 1930’s and 1940’s to help manage quality. Subsequently,
progress in continuous quality improvement in Japan led to significant expansion
of the many simple statistical tools on shop floor. Kaoru Ishikawa, head of the
Japanese Union of Scientists and Engineers (JUSE), later formalized the use of
these  tools  in  Japanese  manufacturing  with  the  introduction  of  the  7  Quality
Control (7 QC) tools. The seven Ishikawa tools reviewed below are now an integral
part of quality control on the shop floor around the world. Many Indian industries
use them routinely. Some of these quality improvements tools were discussed
earlier in the first Part.

Flowchart

The  flowchart  lists  the  order  of  activities  in  a  project  or  process  and  their
interdependency.  It  expresses  detailed  process  knowledge.  To  express  this
knowledge  certain  standard  symbols  are  used.  The  oval  symbol  indicates  the
beginning or end of the process. The boxes indicate action items while diamonds
indicate decision or check points. The flowchart can be used to identify the steps
affecting quality and the potential control points. Another effective use of the
flowchart would be to map the ideal process and the actual process and to identify
their differences as the targets for improvements. Flowcharting is often the first
step in Business Process Reengineering (BPR).

164

Histogram

The  histogram  is  a  bar  chart  showing  a  distribution  of  variable  quantities  or
characteristics. An example of a “live” histogram would be to line up by height a
group of students enrolled in a course. Normally, one individual would be the
tallest  and  one  the  shortest,  with  a  cluster  of  individuals  bunched  around  the
average height.

In manufacturing, the histogram can rapidly identify the nature of quality problems
in a process by the shape of the distribution as well as the width of the distribution.
It informally establishes process capability. It can also help compare two or more
distributions.

Pareto Chart

The Pareto chart, indicates the distribution of effects attributable to various causes
or factors arranged from the most frequent to the least frequent. This tool is named
after Wilfred  Pareto,  the  Italian  economist  who  determined  that  wealth  is  not
evenly distributed and some of the people have most of the money.

This tool is a graphical picture of the relative frequencies of different types of
quality problems with the most frequent problem type obtaining dear visibility.
Thus the Pareto chart identifies the vital few and the trivial many and it highlights
problems that should be worked first to get the most improvement. Historically,

Cause and Effect Diagram

The  cause  and  effect  diagram  is  also  called  the  fishbone  chart  because  of  its
appearance and the Ishikawa diagram after the man who popularized its use in
Japan. Its most frequent use is to list the causes of some particular quality problem
or defect. The lines coming of the core horizontal line are the main causes while
the lines coming off those are sub causes.

The  cause  and  effect  diagram  identifies  problem  areas  where  data  should  be
collected and analysed. It is used to develop reaction plans to help investigate
out-of-control points found on control charts. It is also the first step for planning
design of experiments (DOE) studies and for applying Taguchi methods to improve
product and process designs.

Scatter Diagram

The scatter diagram shows any existing pattern in the relationship between two
variables that are thought to be related. For example, is there a relationship between
outside temperature and cases of the common cold? As temperatures drop, do
cases of the common cold rise in number? The closer the scatter points hug a
diagonal  line,  the  more  closely  there  is  one-to-one  relationship  between  the
variables being studied. Thus, the scatter diagram may be used to develop informal
models to predict the future based on past correlations.

Run Chart

The run chart shows the history and pattern of variation. It is plot of data points in
time sequence, connected by a line. Its primary use is in determining trends over
time. The analyst should indicate on the chart whether up is good or down is

Statistical Quality
Control

165

Tools and Techniques

good. This tool is used at the beginning of the change process to see what the
problems are. It is also used at the end (or check) part of the change process to see
whether the change made has resulted in a permanent process improvement.

Control Chart

Whereas a histogram gives a static picture of process variability, a run chart or a
control chart illustrates the dynamic pet romance (i.e., performance over time) of
the process. The control chart in particular is a powerful process quality monitoring
device and it constitutes the core of statistical process control (SPC). It is a line
chart marked with control limits at 3 standard deviations (s) above and below the
average quality level.

These limits are based on the statistical studies of shop data conducted in the
1930s by Dr Walter Shewart.

Failure to distinguish between common causes and special causes of variation
can actually increase the variation in the output of a process. This is often due to
the mistaken belief that whenever process output is off target, some adjustment
must be made. However, knowing when to leave a process alone is an important
step in maintaining control over a process. Equally important is deciding when to
take action to prevent the production of nonconforming product. Using actual
industry data Shewhart demonstrated that a sensible strategy to control quality is
to  first  eliminate  the  special  causes  with  the  help  of  the  control  and  then
systematically reduce the common causes. This strategy reduces the variation in
process output with a high degree of reliability while it improves the acceptability
of the product.

Statistical process control (SPC) is actually a methodology for monitoring a process
to(a)  identify  the  special  causes  of  variation  and  (b)  signal  the  need  to  take
corrective  action  when  it  is  appropriate. When  special  causes  are  present,  the
process is deemed to be out of control. If the variation in the process is due to
common causes alone, the process is said to be in statistical control. A practical
definition of statistical control is that both the process averages and variances are
constant over time . Such a process is stable and predictable.

SPC uses control charts as the basic tool to improve both quality and productivity.
SPC provides a means by which a firm may demonstrate its quality capability, an
activity necessary for survival in today’s highly competitive markets. Also, many
customers (e.g., the automotive companies) now require the evidence that their
suppliers use SPC in managing their operations. Note, however, that since SPC
requires processes to display measurable variation; even though it is quite effective
for  companies  in  the  early  stages  of  quality  efforts,  it  becomes  ineffective  in
producing improvements once quality level approaches six-sigma.

7.4 CONTROL CHARTS

As we mentioned in the previous section, the control chart is a powerful process
quality monitoring device and it constitutes the core of statistical process control
(SPC).  In  SPC  methodology  knowing  when  to  leave  a  process  in  itself  is  an
important step in maintaining control over a process. Control charts enable us to
do that.

166

Equally important is knowing when to take action to prevent the production of
nonconforming product.

Statistical Quality
Control

Indeed, failure to distinguish between variation produced by common causes and
special causes can actually increase the variation in the output of a process. Again,
control charts empower us here.

When the chart crosses any of its control limits, special causes are indicated to be
present. The process is now deemed to be out of control and is investigated to
remove the source of disturbance. Otherwise, when variation stays within control
limits, it is indicated to be due to common causes only. Now the process is said to
be in “statistical control” and it should be left alone. Statistical control is defined
as the state in which both the process averages and variances are constant over
time and hence the process output is stable and predictable. Control charts help
us in bringing a process within such control.

Most  processes  that  deliver  a  “product”  or  a  “service”  may  be  monitored  by
measuring  their  output  over  time  and  then  plotting  these  measurements
appropriately. However, processes differ in the nature of those outputs. Variables
data are those output characteristics that are measurable along a continuous scale.

Examples of variables data are length, weight, or viscosity. By contrast, some
output may only be judged to be good or bad, or “acceptable” or “unacceptable”,
such as print quality of a photocopier or defective knots produced per meter by a
weaving machine. In such cases we categorize the output as an attribute that is
either acceptable or unacceptable; we cannot put it on a continuous scale as done
with weight or viscosity.

However, SPC methodology provides us with a variety of different types of control
charts to work with such diversity.

For variables data control charts most commonly used are the “x˜” chart and the
“R-chart” (range chart). The x chart is used to monitor the centring of the process
to help control its accuracy . The R-chart monitors the dispersion or precision of
the process.Range R rather than standard deviation is used as a measure of variation
simply to enable workers on the factory floor perform control chart calculations
by  hand,  as  done  for  example  in  the  turbine  blade  machining  shop  in  BHEL,
Hardwar. For large samples and when data can be processed by a computer. The
standard deviation is a better measure of variability.

Interpreting Abnormal Patterns in Control Charts

When a process is in statistical control the points on a control chart fluctuate
randomly between the control limits with no recognizable, non-random pattern.
The following checklist provides a set of general rules tor examining a process to
determine if it is in control:

1. No points are outside control limits.

2. The number of points above and below the center line is about the same.

3. The points seem to fall randomly above and below the center line.

4. Most points, but not all, are near the center line, and only a few are dose to

the control limits.

167

Tools and Techniques

168

The underlying assumption behind these rules is that the distribution of sample
means  is  normal.  This  assumption  follows  from  the  central  limit  theorem  of
statistics, which states that the distribution of sample means approaches a normal
distribution as the sample size increases regardless of the original distribution.
Of course, for small sample sizes, the distribution of the original data must be
reasonably normal for this assumption to hold. The upper and lower control limits
are  computed  to  be  three  standard  deviations  from  the  overall  mean.  Thus,
probability that any sample mean falls outside the control limits is very small.
This probability is the origin of rule 1.

Since the normal distribution is symmetric, about the same number of points fall
above as below the centre line. Also, since the mean of the normal distribution is
the median, about half the points fall on either side of the centre line. Finally, about
68 percent of a normal distribution falls within one standard deviation of the mean;
thus, most but not all points should be close to the centre line, These characteristics
will hold provided that the mean and variance of the original data have not changed
during the time the data were collected; that is, the process is stable.

Several types of unusual patterns arise in control charts, which are reviewed here
along with an indication of the typical causes of such patterns.

One Point Outside Control Limits

A single point outside the control limits is usually produced by a special cause.
Often, the R-chart provides a similar indication. Once in awhile, however, such
points are normal part of the process and occur simply by chance.

A common reason for a point falling outside a control limit is an error in the
calculation of x bar or R for the sample. You should always check your calculations
whenever this occurs, other possible cause area sudden power surge, a broken
tool, measurement error, or an incomplete or omitted operation in the process.

Sudden Shift in the Process Average

An unusual number of consecutive points falling on one side of the centre line
are usually an indication that the process average has suddenly shifted. Typically,
this occurrence is the result of an external influence that has affected the process,
which would be considered a special cause. In both the x bar and R-charts, possible
causes might be a new operator, a new inspector, a new machine setting, or a
change in the setup or method.

If the shift is up in the R-chart, the process has become less uniform. Typical
causes are carelessness of operators, poor or inadequate maintenance, or possibly
a fixture in need of repair. If the shift is down in the R-chart, the uniformity of the
process  has  improved.  This  might  be  the  result  of  improved  workmanship  or
better  machines  or  materials. As  mentioned,  every  effort  should  be  made  to
determine the reason for the improvement and to maintain it.

Three rules of thumb are used for early detection of process shifts. A simple rule
is that if eight consecutive points fall on one side of the centre line, one could
conclude that the mean has shifted. Second, divide the region between the centre
line  and  each  control  limit  into  three  equal  parts.  Then  if  (a)  two  of  three
consecutive points fall in the outer one-third region between the centre line and

one of the control limits or (b) four of five consecutive points fall within the outer
two-thirds region, one would also control that the process has gone out of control.

Statistical Quality
Control

Cycles

Cycles are short, repeated patterns in the chart, alternating high peaks and low
valleys These  patterns  are  the  result  of  causes  that  come  and  go  on  a  regular
basis. In the x bar chart, cycles maybe the result of operator rotation or fatigue at
the end of a shift, different gauges used by different inspectors, seasonal effects
such as temperature or humidity or differences between day and night shifts. In
the R-chart cycles can occur from maintenance schedules, rotation of fixtures or
gages, differences between shifts, or operator fatigue.

Trends

A trend is the result of some cause that gradually affects the quality characteristics
of the product and causes the points on a control chart to gradually move up or
down from the centre line. As a new group of operators gains experience on the
job, for example, or as maintenance of equipment improves over time, a trend
may occur. In the x bar chart, trends may be the result of improving operator
skills,  dirt  or  chip  build-up  in  fixtures,  tool  wear,  changes  in  temperature  or
humidity, or aging of equipment. In the R-chart, an increasing trend may be due
to a gradual decline in material quality, operator fatigue, gradual loosening of a
fixture or a tool, or dulling of a tool. A decreasing trend often is the result of
improved operator skill or work methods, better purchased materials, or improved
or more frequent maintenance.

Hugging the Centre Line

Hugging the centre line occurs when nearly all the points fall dose to the centre
line In the control chart it appears that the control limits are too wide. A common
cause of hugging the centre line is that the sample includes one item systematically
taken from each of several machines, spindles, operators, and so on. A simple
example will serve to illustrate this pattern.

Hugging the Control Limits

This pattern shows up when many points are near the control limits with very few
in  between.  It  is  often,  called  a  mixture  and  is  actually  a  combination  of  two
different  patterns  on  the  same  chart. A  mixture  can  be  split  into  two  separate
patterns.

A mixture pattern can result when different lots of material are used in one process,
or when parts are produced by different machines but fed into a common inspection
group.

Instability

Instability is characterized by unnatural and erratic fluctuations on both sides of
the chart over a period of time. Points will often lie outside both the upper and
lower control limits without consistent pattern. Assignable causes may be more
difficult to identify in this case than when specific patterns are present. A frequent
cause of instability is over adjustment of a machine, or the same reasons that
cause hugging the control limits.

169

Tools and Techniques

170

As suggested earlier, the R-chart should be analysed before the x bar chart, because
some out-of-control conditions in the R-chart may cause out-of-control conditions
in the chart. Also, as the variability in I the process decreases, all the sample
observations will be closer to the true population mean, and therefore their average,
x bar, will not vary much from sample to sample. If this reduction in the variation
can be identified and controlled, then new control limits should be computed for
both charts.

Routine Process Monitoring and Control

After a process is determined to be in control, the charts should be used on a daily
basis  to  monitor  production,  identify  any  special  causes  that  might  arise,  and
make corrections as necessary. More important, the chart tells when to leave the
process  alone.  Unnecessary  adjustments  to  a  process  result  in  non-productive
labour, reduced production, and increased variability of output.

It is more productive if the operators themselves take the samples and chart the
data. In this way, they can react quickly to changes in the process and immediately
make adjustments. To do this effectively, training of the operators is essential.
Many companies conduct in-house training programmes to teach operators and
supervisors the elementary methods of statistical quality control. Not only does
this training provide the mathematical and technical skills that are required, but it
also give the shop floor personnel increased quality consciousness.

Introduction of control charts on the shop floor typically leads to improvements
in conformance, particularly when the process is labour intensive.

Another important point must be noted. Control charts are designed to be used by
production  operators  rather  than  by  inspectors  or  QC  personnel.  Under  the
philosophy  of  statistical  process  control,  the  burden  of  quality  rests  with  the
operators themselves. The use of control charts allows operators to react quickly
to special causes of variation. The range is used in place of the standard deviation
for the very reason that it allows shop-floor personnel to easily make the necessary
computations  to  plot  points  on  a  control  chart.  The  right  approach  taken  by
management in ingraining the correct outlook among the workers appears to hold
the key here.

Estimating Plant Process Capability

After a process has been brought to a state of statistical control by eliminating
special causes of variation, the data may be used to find a rough estimate process
capability. This approach uses the average range R bar rather than the estimated
standard  deviation  of  the  original  data.  Nevertheless,  it  is  a  quick  and  useful
method, provided that the distribution of the original data is reasonably normal.

Use of Warning Limits

When a process is in control, the x bar and R charts may be used to make decisions
about the state of the process during its operation. We use three zones on the
charts to help in the routine management of the process. The zones are marked on
the charts as follows.

Zone 1 (it falls between the upper and lower WARNING LINES (or ± 2 sigma
lines).  If  the  plotted  points  fall  in  this  zone,  it  indicates  that  the  process  has

remained stable and actions or adjustments are unnecessary. Indeed any adjustment
here may increase the amount of variability.

Statistical Quality
Control

Zone 2 (it falls between Zone 1 and Zone 3). Any point found in Zone 2 suggests
that there may have been an assignable change and another sample must be taken
to check that out.

Zone 3 (it falls beyond the upper or Lower Control Limit). Any points falling in
this zone indicate that the process should be investigated and that if action is
taken, the latest estimate of x-double bar value and R bar should be used to revise
the control limits.

7.5 CONTROL CHARTS FOR ATTRIBUTES

Attributes  quality  data  assume  only  two  values  of  good  or  bad,  pass  or  fail.
Attributes usually cannot be measured, but they can be observed and counted and
are useful in quality management in many practical situations. For instance, in
printing packages for consumer products, colour quality can be rated as acceptable
or not acceptable, or a sheet of cardboard is either damaged or is not. Usually,
attributes data are easy to collect, often by visual inspection. Many accounting
records, such as percent scrapped, are also usually readily available. However,
one drawback in using attributes data is that large samples are necessary to obtain
valid statistical results.

7.6 CHOOSING THE CORRECT SPC CHART

Confusion often exists over which chart is appropriate for a specific application,
since the c- and u-charts apply to situations in which the quality characteristics
inspected do not necessarily come from discrete units.

The key issue to consider is whether the sampling unit is constant. For example,
suppose  that  an  electronics  manufacturer  produces  circuit  boards.  The  boards
may contain various defects, such as faulty components and missing connections.
Because  the  sampling  unit  -  the  circuit  board  -  is  constant  (assuming  that  all
boards are the same), a c-chart is appropriate. If the process produces boards of
varying sizes with different numbers of components and connections, then a u-
chart would apply.

As another example, consider a telemarketing firm that wants to track the number
of calls needed to make one sale. In this case, the firm has no physical sampling
unit.  However,  an  analogy  can  be  made  with  the  circuit  boards.  The  sale
corresponds to the circuit board, and the number of calls to the number of defects.
In both examples, the number of occurrences in relationship to a constant entity
is being measured. Thus a c-chart is appreciated.

7.7 ACCEPTANCE SAMPLING

Acceptance sampling is a method used to distinguish between acceptable and
poor quality products, but it does not actually improve the quality of the products.
If it were possible to inspect or use every product, a 100% inspection would be
performed, and acceptance sampling would not be necessary. However, 100%

171

Tools and Techniques

inspection is often not feasible or cost-effective, particularly for low-cost mass-
produced items such as injection-moulded parts or flash light bulbs, where the
cost of inspection may exceed the value of the product. In such cases, acceptance
sampling can be used, where a small fraction of the product is inspected using a
sampling plan.

A sampling plan outlines the procedure for drawing a sample from a batch of
products and deciding whether to accept or reject the entire batch based on the
results of the sample inspection. The sample size is typically smaller than the
whole batch, and rejection of the batch may involve downgrading it, selling it at
a lower price, or returning it to the supplier.

For example, a sampling plan may specify that a random sample of n items is
drawn from a batch, and the batch is rejected only if c or more of these n items are
defective or non-conforming. The operating characteristic curve (OC-curve) of a
sampling plan is a graph that shows the probability of accepting the batch (Pa(p))
as a function of the fraction p of defective products in the batch. A higher Pa(p)
benefits the producer, while a smaller Pa(p) benefits the consumer who seeks
assurance against receiving poor quality products and prefers to accept batches
with lower Pa(p)  (fraction defective) values.

AQL and BQL

To specify a sampling plan with the desired Pa(p) characteristics, the values of n
and c must be appropriately determined. This determination involves specifying
two  key  quality  parameters:  the AQL  (acceptable  quality  level)  and  the  RQL
(rejection quality level). The AQL represents the maximum acceptable level of
defects in a batch, while the RQL represents the minimum level of defects that
would result in a batch being rejected.

A perfect quality batch with no defective items is often considered unattainable.
Therefore, customers typically tolerate a small fraction of defective items in their
purchases, as long as the fraction does not exceed the AQL. However, customers
also require a high level of assurance that the sampling plan will reject batches
with fractions of defective items that exceed a poor quality threshold, represented
by the RQL.

The RQL is the defect level that would cause significant issues once a lot enters
the customer’s factory. In contrast, the supplier of the parts aims to ensure that
the customer’s acceptance sampling plan will not reject too many batches that
fall within the customer’s acceptable defect level, represented by the AQL. The
AQL represents the worst fraction of defective items that the customer can accept
on average in the shipments they receive.

The Operating Characteristic (OC) Curve of a Sampling Plan

A bit of thinking will indicate that only error-free 100% inspection of all items in
a lot would accept the batch with 100% probability if the fraction of defective
items in it is less than or equal to AQL and reject the lot with a 100% probability
if the fraction of defective items in it is larger than AQL. Such performance cannot
be realized otherwise.

172

In order to correctly evaluate the OC-curve of an arbitrary (not 100% inspection)

sampling  plan  with  parameters  (n,  c),  we  need  to  use  certain  principles  of
probability theory. Suppose that the batch is large or the production process is
continuous, so that drawing a sample item with or without replacement has about
the same result. In such cases, we can assume that the number of defective items
x in a sample of sufficiently large size n follows a binomial probability distribution.

Now, if the producer is willing to sacrifice a little so that the batch with fraction
defective AQL is accepted with a probability of at least (1-a), where a is a small
positive number, and the consumer is willing to sacrifice a little so that the batch
with fraction defective RQL is accepted with a probability of at most b, where b
is a small positive number and RQL > AQL, then the following two inequalities
can be established.

From  the  above  two  inequalities,  the  numbers  n  and  c  can  be  solved  (but  the
solution may not be unique). The number ‘a’ is called the producer’s risk, and the
number ‘ b’ is called the consumer’s risk. As a common practice in industries, the
magnitude of a & b is usually set at some value from 0.01 to 0.1. Nomo-gram is
available for obtaining solution(s) of the inequalities given above easily.

The sampling plan is called a single sampling plan because the decision to accept
or reject the batch is made in a single stage after drawing a single sample from
the batch being evaluated.

Another  type  of  sampling  plan,  which  is  different  from  the  above,  is  called
continuous  sampling  procedure  (CSP). The  rationale  of  CSP  is  that  if  we  are
unsure about the quality of products produced from a process, a 100% inspection
will be adopted. If the quality of products is found to be good, only a fraction of
the products will be inspected. In the simplest CSP, initially, 100% inspection is
performed.  During  100%  inspection,  if  no  defective  items  are  found  after  a
specified  number  of  items  are  inspected  (which  means  that  the  quality  of  the
product produced is perhaps good), 100% inspection is stopped, and only a fraction
f of the products is inspected. During fraction inspection, if a defective item is
found (which means that the quality of products might have deteriorated), then
fraction inspection is stopped, and 100% inspection is resumed. More refined
CSPs  have  also  been  constructed,  for  example,  by  setting  f  at  1/2  at  the  first
stage, 1/4 at the second stage, and so on.

Variables Sampling Plans

The sampling plans described above are called attribute sampling plans because
the inspection procedure is based on a “go”/”no go” basis, meaning an item is
either considered non-defective and accepted, or it is considered defective and
rejected.  Variable  sampling  plans  are  different  from  attribute  sampling  plans
because continuous measurements, such as dimensional or weight checks, are
made on each item in the sample. The decision to accept or reject the batch is
then  based  on  the  sample  mean  or  the  average  of  the  measurements  obtained
from all items contained in the sample. Variable sampling plans can be used, for
instance, when a product item is deemed acceptable if a certain measurement x
(e.g., diameter, length, hardness) exceeds a pre-set lower specification limit L;
otherwise, the item is considered not acceptable.

Statistical Quality
Control

173

Tools and Techniques

7.8

 SUMMARY

SPC aims at controlling the variability of process output using a device called the
control chart. On a control chart, a certain characteristic of the product is plotted.
Under normal conditions, these plotted points are expected to vary in a “usual
way” on the chart. When abnormal points or patterns appear on the chart, it is a
statistical indication that the process parameters or production conditions might
have changed undesirably.

Process capability is the range over which the “natural variation “of a process
occurs as determined by the system of common or random causes; that is, process
capability indicates what the process can deliver under “stable “conditions when
it is said to be under statistical control.

It  is important to reiterate that acceptance sampling or sampling inspection is
solely a means of screening to separate batches or lots of high quality products
from those of poor quality. This screening process does provide some level of
assurance of the quality of incoming parts and materials. The use of sampling
plans enables industries to conduct this screening more efficiently than simply
drawing samples at random.

As such, sampling inspection can be utilized during purchasing to check the quality
of  incoming  materials  when  there  is  uncertainty  regarding  the  conditions  and
quality control procedures in place at the vendor’s plant. Acceptance sampling
can also be employed for the final inspection of products after production.  This
process, to a limited extent, ensures the quality of the products before they are
dispatched  to  the  customer.  However,  it  is  important  to  note  that  unlike  SPC,
acceptance sampling does not assist in preventing the production of low-quality
products.

7.9 KEY WORDS

Acceptance Sampling

Control Chart

Design of Experiments

Fishbone Chart

inputs

: The process of selecting a sample from
(raw  material,
incoming
components  etc.)  or  semi-finished,  or
finished  products  for  the  purpose  of
analysing the results.

: A line chart showing the control limits at
three  standard  deviations  above  and
below  the  average  quality  level.  It
constitutes the core of SPC.

: Application  of  statistical  methods  for
producing high quality, robust products
and process designs (one of the Taguchi
methods).

: A diagram showing the main causes and
sub-causes of a quality problem or defect.

174

Flow Chart

Histogram

Pareto Chart

Process Capability

: A  device/method  showing  the  order  of
activities  in  a  process  or  a  project  and
their interdependency.

: A Bar Chart showing the distribution of
variable quantities or characteristics.

: A chart showing the distribution of effects
attributable to various causes or factors
arranged  from  the  most  frequent  to  the
least frequent.

: The  range  over  which  the  ‘natural
variation’  of  a  process  occurs  and  is
determined  by  the  system  of  common/
random causes.

Statistical Process Control (SPC) : A  process  to  control  the  variability  of

output using control charts.

Statistical Quality Control (SQC) : Use of statistical methods to improve or
enhance quality for customer satisfaction.

7.10  SELF-ASSESSMENT QUESTIONS

1. Define statistical process control and discuss its advantages

2. What does the term statistical control mean? Explain the difference between

capability and control.

3. What  are  the  disadvantages  of  simply  using  histograms  to  study  process

capability?

4. Discuss the three primary applications of control charts.

5. Describe the difference between variables and attributes data. What types of

control charts are used for each?

6. How should control charts be used by shop-floor personnel?

7. What  are  modified  control  limits?  Under  what  conditions  should  they  be

used?

8. Describe some situtations in which a chart for indiviual measurments would

be used.

7.11  FURTHER READINGS

• Charantimath, P. M. (2017). Total Quality Management. Pearson India.

• Dale, B. G., Bamford, D., & Van Der Wiele, T. (2016). Managing Quality:

An Essential Guide and Resource Gateway. John Wiley & Sons.

• D C Montgomery (1993) Statistical Quality Control, 3rded., John Wiley.

Statistical Quality
Control

175

Tools and Techniques

• M-25 Statistical Process Control Methods: Control Chart for Variables.

(2018). e-PGPathshala. http://epgp.inflibnet.ac.in/Home/
ViewSubject?catid=ahLCajOqz6/GWFCSpr/XYg==

• M-26 Statistical Process Control Methods: Control Chart for Attributes.

(2018). e-PGPathshala. http://epgp.inflibnet.ac.in/Home/
ViewSubject?catid=ahLCajOqz6/GWFCSpr/XYg==

• M-27 Statistical Process Control Methods: various Tools. (2018).e-

PGPathshala. http://epgp.inflibnet.ac.in/Home/
ViewSubject?catid=ahLCajOqz6/GWFCSpr/XYg==

• T P Bagchi (1996) IS0 9000: Concepts, Methods and Implementation,

2" ed., Wheeler.

• Total Quality Management - I. (2017). Management aspects of Quality - II.

NPTEL. https://www.youtube.com/watch?v=jrutd0GZdJE

• Total Quality Management - I. (2017). Introduction to Acceptance Sam-
pling. NPTEL. https://www.youtube.com/watch?v=4QzEWM2pVFY

• Total Quality Management - I. (2017). 7 Old Tools for Quality Assurance .

NPTEL. https://www.youtube.com/watch?v=6-JVHv5djIc

176

UNIT 8 TOOLS AND TECHNIQUES OF TQM

Tools and Texhniques
of TQM

Objectives

After reading this unit, you should be able to:

•

•

•

•

•

•

explain the need for benchmarking;

implement and appreciate the usefulness of Quality Function Deployment
(QFD);

understand the concepts and tools that can be used to improve quality;

appreciate the concept of reliability as a special dimension;

understand the role of  zero defects in  Total Quality Management;

understand the principles and practices of Re-engineering.

Structure

8.1

8.2

8.3

Introduction

Principles of Benchmarking

Types of Benchmarking

8.4 Quality Function Deployment (QFD)

8.5 House of quality (HOQ)

8.6

8.7

8.8

8.9

Reliability

5 ‘S’

Zero Defects (ZD)

Re-engineering

8.10 Taguchi Methods

8.11 Six  Sigma Principle

8.12 Cross Functional Management

8.13 Hypothesis

8.14 Summary

8.15 Keywords

8.16 Self-Assessment Questions

8.17 Further Readings

8.1

INTRODUCTION

TQM employs several tools and techniques. We have discussed few of them. In
this unit we will discuss Benchmarking and, Quality Function Deployment (QFD),
Zero Defects, Reliability, Re-engineering, etc.

177

Tools and Techniques

We now know that Total Quality Management (TQM) is essentially concerned
with  continuous  improvement  of  the  quality  of  goods  and  services  to  satisfy
growing expectations of customers. Such improvements in final deliverables could
only be effectively made when improvements are made in both design and delivery
of  deliverables.  Various  organizational  variables  like  social,  culture,  human
attitude,  technology,  etc.  are  also  required  to  be  suitably  changed  to  effect
improvements in the desired direction. This unit looks at some of these aspects.
Reliability  which  is  an  important  component  of  quality  needs  to  be  assessed,
specified and improved with the help of suitable tools and techniques of reliability
engineering. Reliability, therefore, is a major concern at the design stage. Similarly,
appropriate steps are also required to be taken to improve design specifications,
so that products could work satisfactorily even under adverse conditions, at least
to  a  certain  extent.  Off-line  Quality  Control  by  the  Taguchi  Method  aims  at
developing such robust designs. In spite of having a good design, a product may
not ultimately satisfy customers unless the same is manufactured with sufficient
care on the shop floor. Those working on the shop floor should inculcate good
working habits so that they keep the place clean, properly organized and make
efforts to see that the workplace continues to be pleasant to work at. A Japanese
concept called 5 ‘S ‘has drawn attention to this aspect. Similarly, management
should also be sincere and should continuously facilitate all their employees to
reach a level of perfection. Programmes like ‘ zero defects’ are required to be
taken by the management on a continuous basis. However, such improvements
need  to  be  supplemented  sometimes  by  major  initiatives  which  could  cause
improvements by an order-of-magnitude. Such a kind of initiative is known as
‘Re-engineering’. We shall discuss all the above concepts and techniques in the
following sections.

8.2 PRINCIPLES OF BENCHMARKING

The term Benchmarking has different meanings for different persons. To define
benchmarking, it is “a standard against which something can be measured, i.e. a
“reference point’. The term, as originally coined by Xerox Corporation, U.S.A.,
meant  continuous  process  of  measuring  the  products,  services,  and  practices
against the toughest competitors or organizations, known as ‘leaders’.

This  definition  emphasizes  the  analytical  part  of  the  work  measurement  and
comparison. But one of the subsidiaries of Xerox - Rank Xerox, U.K. looked at it
somewhat differently. It viewed it as a continuous systematic process of evaluating
organizations recognized as industry leaders, for determining business and work
processes that represented best practices. In operational terms, this is frequently
condensed  to  the  search  for  industry  best  practices  that  lead  to  superior
performance’’. ‘Best practices’ means the methods and procedures used in work
processes  that  best  meet  customer  requirements.  Benchmarking  is  not  simply
about what we want to achieve - the benchmarks or the measurements of best
performance,  but  also  how  they  are  achieved  i.e.  processes  in  action.  Thus,
benchmarking  is  an  ongoing  task  at  all  levels  of  business  of  finding  and
implementing the world’s best practices in the key things that are done to deliver
customer satisfaction.

178

The benchmarking process consists of the following three elements or components:

i) Analysis: breaking down an issue into components

Tools and Techniques
of TQM

ii) Comparison:  component-by-component  comparison  to  find  gaps  or

differences.

iii) Synthesis:  Recombination  of  components  with  ideas  stimulated  from  the

differences.

The original concept of benchmarking had been in practice in India about 3000
years ago. The dominant method of learning which was known then to people,
used  to  be  watching  the  actions  of  leaders.  Foot  prints  of  wise  men  are  what
common people are told to follow. Such a principle of learning got subsequently
spread to other countries like Japan, and transformed the principle into a practical
application in an industrial context. Japan calls it ‘Dantatsu’, a method of choosing
the best of the best. Subsequently, US organization, faced with severe competition
from Japanese organizations, made use of this principle to develop a structured
method of adaptive innovation and termed it as ‘Benchmarking’.

8.3 TYPES OF BENCHMARKING

Since benchmarking is essentially learning from comparison with others, it is
categorized into different types depending upon either objects being compared or
in respect of units with which comparison is made.

Based on the objects to be benchmarked, benchmarking has been classified into
four categories. These categories are as follows:

• Product Benchmarking

• Performance Benchmarking

• Process Benchmarking

• Strategic Benchmarking

Product  Benchmarking:  This  is  also  alternatively  termed  as  ‘Customer
Satisfaction Benchmarking’ or ‘Customer Value Profiling’. This refers to both
engineering and qualitative comparison of products and services among competing
offerings. Many of the manufacturing organizations have been doing several kinds
of  reverse  engineering  to  benchmarking  various  features  of  their  products.
Recently, several organizations especially in the service sector have shown their
concern in comparing their services with others. Product Benchmarking can also
help  in  identifying  activities  where  improvement  is  possible.  Product
Benchmarking quite often leads to the redesign of existing products and services.

Performance Benchmarking: Performance benchmarking refers to comparison
of performance indicators related to a business as a whole or a group of critical
activities  or  processes.  Business  level  performance  benchmarking  which  was
previously used under the banner of ‘inter-organization comparison’ done through
a set of well defined financial ratios, has again drawn the attention of world class
organizations. It has been found to be a very important tool to identify different
functional areas where scope for improvement is high. However, such business
level comparison now includes many performances issues like innovativeness of

179

Tools and Techniques

the organization, customer satisfaction from the product and services delivered
by the organizations, etc.

Process  level  performance  benchmarking  includes  comparison  of  process
performance  indicators  in  terms  of  those  issues  which  are  critical  to  the
implementation of business strategy. These indicators relate to resource efficiency,
resource allocations and many other issues which are relevant for the processes
under reference. Performance benchmarking is becoming very important tool to
provide external feedback to the concerned persons involved in the process or in
any of the constituent activities.

Though  improvement  is  implicit  in  performance  benchmarking  of  both  kinds
mentioned above, there is no explicit attempt to design any new course of action
as part of performance benchmarking.

Process Benchmarking: This refers to comparison of processes. A process is a
set of sequential activities as performed on an item to increase its value to the
customers.  There  are  three  major  categories  of  processes  -  business  process,
support  process  and  management  processes,  depending  upon  the  nature  of
customers served. In a developed country where competition in product market
has become fierce, business process benchmarking is fast becoming a standard
management tool to maintain market share.

Process  benchmarking  requires  explicit  conduct  of  all  three  elements  of
benchmarking as mentioned above. In other words, it leads to the redesign of
new processes to be implemented by the management.

Strategic Benchmarking: This refers to a study of corporate level or business
level  strategies  pursued  by  some  of  the  selected  organizations  reputed  for
reformulation of strategies or polices in recent times. Many of the top managements
have been constantly reviewing the business portfolios of their organizations.

Benchmarking corporate strategies of other successful organizations could give
some additional insights in their efforts. Business strategies refer to the direction
in which a specific business is moving to ensure its attractiveness to customers
and  other  stockholders. An  organization  could  study  the  business  strategy  of
another successful business and use the strategy for building up the attractions.
Such strategic benchmarking will gain more and more significance as markets
become competitive.

Based on the organizations against whom one is benchmarking, benchmarking
methodology could again be categorized into five following types :

i)

Internal  Benchmarking  -  Comparison  between  department,  plants,
subsidiaries  etc.  within  the  country  or  among  the  countries  through
collaborations.

ii) Industry Benchmarking - Comparison of performances by the organizations

producing the same class of products and services.

iii) Competitive  Benchmarking  -  Comparison  of  performance  against  direct

competitors.

180

iv) Best-in-class Benchmarking - Comparison with best practices prevalent in

an organization irrespective of products and services.

Tools and Techniques
of TQM

v) Relationship Benchmarking - Comparison is made with an organization
with which the benchmarking organization already has a relationship like
customer-supplier relations, joint venture arrangement, etc.

Product Benchmarking

This refers to comparison of different features and attributes of competing products
and services either through engineering analysis or through analyses of perception
of customers. Engineering approach of product benchmarking was in practice for
quite some time. This method, normally known as reverse engineering, is basically
technical, engineering based approach comprising of tear-down and evaluation
of  technical  product  characteristics.  Most  of  the  consumer  goods  and  capital
equipment manufacturing organizations have one or other way, been doing reverse
engineering to finalize product specifications. Some of the Indian organizations
also carried out value analysis in conjunction with reverse engineering. Value
analysis  facilitates  searching  for  cost-effective  alternatives  for  the  chosen
components  or  sub-assemblies,  specifications  of  which  are  found  out  through
comparison  process. An  engineering  department  equipped  with  tools  of  value
engineering, can develop suitable for developing product specifications that are
comparable, if not better, to competitive offerings.

Comparison of customer-perceived-quality assumed great significance during the
1970’s when it was revealed to be the most important factor for market share in
competitive  economic  conditions.  It  was  observed  that  customers  made  their
judgment relative to value i.e. quality and price. The relative perceived quality is
a quality from the customer perspective, with respect to alternative competitive
offerings in the market.

Products and services provided by some organizations are of much lower perceived
quality compared to world class offerings. Under this situation, one can easily
perceive use of product benchmarking to identify immediate priority areas for
improvement. This should be done on continuous basis so that all the important
attributes as sought by customers are supplied through their offerings, thereby
increasing  relative  customer-perceived-quality  and,  in  turn,  increasing  market
share.

Though some marketing departments of Indian organizations have been doing
some form of product perception analysis, many of such analyses fall short of
requirements  as  mentioned  above.  Further,  it  has  been  found  that  product
benchmarking should be done by an inter-disciplinary group instead of marketing
departments alone, to provide maximum benefits.

Performance Benchmarking

It is alternatively known as ‘Result Benchmarking’ or ‘Benchmark Studies’ as
benchmarking often includes/ business or process outcomes. It is also termed as
‘industry benchmarking’ as participants of such a study often belong to a single
industry.

For  this  kind  of  benchmarking,  all  the  different  kinds  of  system  performance

181

Tools and Techniques

variables - efficiency, effectiveness, productivity, quality of work life, flexibility,
innovativeness and profitability could be measured and compared either for a
whole business or for any of the constituent functions or processes. Criticality in
a business context decides which variables out of all the above mentioned ones
are relevant and of common interest to all the participating organizations in a
performance benchmarking study.

Performance  benchmarking  which  was  used  to  be  known  earlier  as
‘Interorganization Comparison’ has been in practice in India since 1960s. In some
of the industries like Textile, Fertilizer etc., performance benchmark’s were in
vogue. However, such comparisons included mostly financial ratios at aggregate
levels  and  were  often  used  for  management  control  purposes.  Performance
benchmarking which has recently been prompted by the National Productivity
Council of India includes all the strategic and critical issues both at business and
funded  levels  that  are  current  concern  of  managements  of  participating
organizations.  These  issues  are  expressed  either  in  financial  or  in  operational
terms.

Process Benchmarking

It is now realised that it is not enough to know ‘where’ an organization is but it is
also  important  to  know  ‘how  ‘and  ‘why’  it  has  reached  that  stage.  Process
benchmarking  provides  us  with  a  more  effective  and  efficient  process  to  be
implemented. A process is a set of sequential activities performed on an item to
add value to the item for creating customer satisfaction. Process benchmarking is
a complete method containing all the elements of ideal benchmarking process
i.e. analysis, comparison and synthesis. It is, thus, an essential tool when an existing
process is to be redesigned or re-engineered.

There  are  many  models  available  in  the  West  regarding  the  appropriate
methodology to carry out process benchmarking. National Productivity Council
(NPC) of India has evolved a 8 step process to suit Indian conditions. According
to the NPC mode1, process benchmarking methodology, to be carried out by a
process oriented benchmarking team, consists of the following steps:

Step 1 :

Identify the object or process to be redesigned or improved.

Step 2 : Map and measure the existing process in its entirety in terms of relevant

critical dimensions.

Step 3 :

Identify  the  partner  where  the  same  process  is  known  to  be  better
performed.

Step 4 : Analyse the partner’s process and find out the differences. This often
requires collection of data through a check list/questionnaire and/or
physical visit to the partner’s site.

Step 5 : Redesign the process and put up the proposal for management approval.

Step 6 :

Implement the re-designed process .

Step 7 : Monitor the performance of the redesigned process.

182

Step 8 : Recalibrate the process.

Though the benchmarking partner could belong to the same organization or to
the same industry, any major change in the process performance could be achieved
when the partner is drawn from an organization whose products and services are
quite dissimilar. However, in such benchmarking, acceptance by the organization
personnel could be an important factor.

Several studies have shown that almost all the leading American and European
organizations have gone for process benchmarking. In India and every process
provides scope as each has been established based on traditional management
thinking. An  organization  normally  has  three  kinds  of  processes;  business
processes, support processes and management processes. The business process
linking  the  organization,  directly  with  customers  is  a  high  priority  area  for
benchmarking in a highly competitive situation. But, quite often, an improved
business  process  like  distribution,  customer  service  provision,  etc.  cannot  be
sustained over a long time if supportive processes are not equally efficient. So,
support processes like procurement, manufacturing, machinery maintenance, etc.
are required to be improved or re-engineered before an efficient business process
is fully functional to its optimum performance level. In Indian circumstances,
support processes should be priority areas for improvement. These also include
management processes.

Strategic Benchmarking

Strategy is the ability to see where one wants to go, and to do things necessary to
stay on track and get there.

Using this definition, strategy is both forward-looking (proactive) and side-looking
(reactive). Looking around and learning from others are thus important enablers
for such strategy planning.

Strategic thinking in business is the matching of a business’s opportunities with
its resources in order to develop a direction. Such thinking is often reflected in a
strategic plan that specifies goals and objectives and areas for resource allocation.
Strategic  benchmarking  addresses  all  the  pertinent  issues  involved  in  the
abovementioned strategic planning.

It is only during the 1990’s that many Indian organizations have been seriously
pursuing strategic planning and carrying out competitor’s analysis. An established
quantitative  method  of  strategic  benchmarking  has  been  developed  with  the
application of PIMS (Profit Impact of Market Strategy) model containing up-to-
date strategic information of 3000 business units.

Alternatively, strategic benchmarking could also be carried out by the application
of process benchmarking techniques and methods. Many strategic consultants in
the West have now observed that strategic benchmarking is similar in application
to benchmarking of work processes, but different in scope.

8.4 QUALITY FUNCTION DEPLOYMENT (QFD)

The level of competition is intensifying as the business environment shifts from
national to global. This increase in competition has often focused on developing
new and improved products to meet customers’ specific needs. This is forcing

Tools and Techniques
of TQM

183

Tools and Techniques

184

organizations to match or surpass their competitors’ products in terms of quality,
price and service in order to survive. As customers become more value conscious
and selective in the products they buy, organizations have begun to focus their
attention  on  ways  in  which  they  could  attain  long-term  market  share  and
profitability through enhanced product development practices.

Examining how successful organizations develop their products may helpful to
managers  in  understanding  adopting  benchmarking  of  their  own  product
development methods in their organizations. Quality

Function Deployment (QFD) has been heralded as an important tool of the product
development process.QFD enables an organization to measure customer ‘wants’
and map them against the engineering ‘how’ in a way that highlights trade-offs
and drives the product’s design toward customer requirements.

The importance of meeting customers’ quality requirements has steadily migrated
upstream through the manufacturing process since the final inspection era of the
1920s. As the cost of producing nonconforming products has risen (in terms of
production cost, warranty claims, lost sales, etc.), organizations have attempted
to identify the root causes. Statistical Process Controls (SPC), introduced in the
army forces during World War II, and was one of the first methods used to reduce
the number of defective products. SPC gained industry acceptance during the
last 1950s and early 1960s and remained the most common form of quality control
in the United States until the 1970s. While SPC can reduce the number of defective
products that reach the customer, it is still a reactive quality control measure.

Designing  quality  into  the  product  through  improvements  in  the  product
development  process  and  building  robustness  into  the  production  system  by
designing products for easy manufacturing and assembly became important issues
in the US during the 1980s. Addressing quality, production, and customer issues
while still in the design stage of product development allows organizations to
realize greater savings while attaining higher product quality. As the intensity of
competition  increases,  organizations  use  cross  functional  teams  with
representatives from marketing, manufacturing, suppliers and final customers to
design, market and manufacture products. This front-loading of quality allows
organizations to develop and maintain a competitive advantage over competitors
who follow the traditional ‘over-the-wall’ approach to product development.

QFD,  which  was  first  used  at  Mitsubishi’s  Kobe  shipyard  site  in  1972,  was
designed as a tool to facilitate a cross-functional product development process.
The application of QFD by Japanese organizations accelerated through the 1980s.
The acclaimed benefits of using QFD (lower production cost, shorter development
time, and higher quality) attracted a few US organizations in the mid to late 1980s.
This gap between Japanese and US implementation of QFD methods may help to
explain  the  superiority  of  Japanese  products  and  the  growth  of  Japanese
organizations’ market share during this time period.

What is QFD?

Quality  Function  Deployment  has  been  defined  as  a  system  for  translating
consumer requirements into appropriate organization requirements at each stage

from  research  and  product  development  to  engineering  and  manufacturing  to
marketing/sales  and  distribution  (American  Supplier  Institute,  1989).  QFD  is
taking the voice of the customer from the beginning of product development and
deploying it throughout the organization through a sequence of phases. In QFD,
the voice of customer aligns the organization’s resources to focus on maximizing
customer satisfaction and minimising waste. QFD is not just a quality tool, it is
also a planning tool for developing new products and improving existing products.

QFD  permits  the  ‘voice  of  the  customer’,  rather  than  the  ‘demands  of
management’,  to  allocate  organization  resources  and  to  coordinate  skills  and
functions in producing the final product. Listening to the customer requires that
the management works to gain an understanding of its customers at three levels.
The first level understands the basic wants and needs of the customer. A cross-
functional  team  using  a  variety  of  market  research  methods  (e.g.  individual
interviews,  focus  groups  and  mail  and  telephone  surveys)  generates  a  list  of
customer requirements. The information collected during this stage is referred to
as the ‘spoken’ quality demands and performance expectations. The requirements
are usually vague (e..g. ‘good ride’) or incomplete and must be further defined
into measurable characteristics. There is also information which is not directly
given  by  the  customer  but  must  be  included  in  the  analysis  to  obtain  a  more
complete understanding of customer requirements. The ‘unspoken’ attributes are
often overlooked by the customer or assumed to be incorporated into the product
(e.g. airplane arrives safely). The product must fulfill all these basic requirements,
along with attaining high levels of performance in order to achieve a competitive
level of customer satisfaction.

Second,  QFD  must  drive  the  organization  to  go  beyond  these  data  collection
techniques and identify fundamental customer needs and root product function.
In addition to the spoken and implied wants of the customer, QFD forces the
design  team  to  determine  hidden  customer  requirements  by  studying  how
customers  use  a  product,  examining  the  product’s  applications  and  learning
customer behaviours. For example, customers may express a desire to have the
bank offer more convenient hours. One response would be to open the bank for
longer hours. Another would be to offer access to its services via a computer
network and automated teller machines.

Third, in addition to learning the basic quality and performance attributes and
root product functions, the product must provide unexpected features which ‘excite
and delight’ the customer in order to sustain long term market share. These features
are  not  usually  known  by  the  customer  because  they  are  either  not  aware  of
technological advances (e.g. new laser applications) or have become accustomed
to standard product uses or applications. While some new characteristics have
evolved from technological breakthroughs, not all new features must come through
research and development. ‘New’ features or product applications are found when
time is spent understanding the customer and how the product is being used. As
new features are introduced and competitors copy or surpass existing products or
services,  characteristics  which  one  surprised  the  customer,  become  standard
product features over time (e.g. air bags in automobiles).

Hence, the list of product characteristics must be continually updated and revised.

Tools and Techniques
of TQM

185

Tools and Techniques

8.5 HOUSE OF QUALITY (HOQ)

Figure 8.1 shows the essential components of the quality table or HOQ diagram.
The construction begins with the customer requirements, which are determined
through the ‘voice of the customer’ - the marketing and market research activities.
These are entered into the blocks to the left of the central relationship activities.
These are entered into the blocks to the left of the central relationship matrix.
Understanding and prioritizing the customer requirements by the QFD team require
the use of competitive and compliant analysis, focus groups, and the analysis of
market potential. The prime or broad requirements should lead to the detailed
WHATs.

Once the customer requirements have been determined and entered into the table,
the important of each is rated, and the rankings are added. The use of the ‘emphasis
technique’ or paired comparison may be helpful here.

Each customer’s requirements should then be examined as per customer rating; a
group  of  customers  may  be  asked  how  they  perceive  the  performance  of  the
organization’s product or service versus those of competitors. These results are
placed  to  the  right  of  the  central  matrix.  Hence  the  customer  requirements,
importance rankings and competition ratings appear from left to right across the
house.

The  WHAT’S  must  now  be  converted  into  the  HOWs.  These  are  called  the
technical design requirements interactions.

186

Figure 8.1: The House of Quality Table

They appear on the diagram from top to bottom in terms of requirements, ranking
(or costs) and ratings against competition. These will provide the ‘voice of the
processes.

Tools and Techniques
of TQM

The technical requirements themselves are placed immediately above the central
matrix and may also be given a hierarchy of prime and detailed requirements.
Immediately below the central relationship matrix appear the rankings of technical
difficulty, development time, or costs. These will enable the QFD team to discuss
the efficiency of the various technical solutions. Below the technical rankings on
the diagram comes the benchmarking data, which compares the technical process
of the organization against its competitors.

The central relationship matrix is the working core of the house of quality diagram.
Here the WHATs are matched with the HOWs, and each customer’s requirement
is systematically assessed against each technical design requirement. The nature
of any relationship-strong positive, neutral, negative, strong negative – is known
by symbols in the matrix. The QFD team carries out the relationship estimation,
using experience and judgment, the aim is to identify HOW so that WHAT may
be achieved. All the HOWs listed must be necessary and together sufficient to
achieve the WHATs. The root of the house shows the interaction between the
technical design requirements. Each characteristic matched against the others,
and the diagram format allows the nature of relationships to be displayed. The
symbols used are the same as those in the central matrix.

The complete QFD process is time-consuming, because each cell in the central
and roof matrices must be examined by the whole learns. The team must examine
the matrix to determine which technical requirement will need design attention,
and the costs of that attention will be given in the bottom row. If certain technical
costs become a major issue, the priorities may then be changed. It will be clear
from the central matrix, if there is more than one way to achieve a particular
customer requirement, and the roof.

HOWs(1)

WHATs
(1)

TARGETs(1)

HOWs(2)

WHATs
(2)

TARGETs(2)

HOWs(3)

WHATs
(3)

TARGETs(3)

Figure 8.2: The ‘Deployment’ of the ‘Voice of Customer’ table

187

Tools and Techniques

matrix will show if the technical requirements to achieve one customer requirement
will have a negative effect on another technical issue.

The very bottom of the house of quality diagram shows the target values of the
technical characteristics, which are expressed in physical terms. They can only
be decided by the team after discussion of the complete house contents. While
these targets are the physical output of the QFD exercise, the whole process of
information-gathering,  structuring,  and  ranking  generates  a  tremendous
improvement in the team’s cross-functional understanding of the product/service
design delivery system. The target technical characteristics may be used to generate
the next level house of quality diagram, where they become the WHAT’s, and the
QFD process determines the further details of HOW they are to be achieved. In
this way the process ‘deploys’ the customer requirements all the way to the final
operational stages. Figure 8.2 show the target technical characteristics at each
level become the inputs to the next level matrix.

An Abridged Example

A lawnmower manufacturer recently spent time and money redesigning a control
for their most popular mower, only to find that customers were insensitive to the
modification. So when they began planning to redesign another of their models,
they wanted to be sure that this time round they would make changes the customer
actually wanted.

1. Product planning matrix

• strong relationship = 3 points

• A medium relationship = 2 points

• weak relationship = 1 points

188

Figure 8.3: QFD for redesigning a lawnmower

The organization carried out market research to find out their customer’s priorities,
and a QFD analysis to see what the implications for design and manufacturing
were. Figure 8.3 gives the details of QFD.

Tools and Techniques
of TQM

The  results  showed  that  customers  were  interested  in  performance  and  that
improving the motor, the drive chain and the efficiency of the blades would have
far more impact than changing the control features which is what was done.

There  should  be  reductions  in  the  number  of  midstream  design  changes,  and
these  reductions  in  turn  will  limit  post-introduction  problems  and  reduce
implementation time. Because QFD is consensus based, it promotes teamwork
and  creates  communications  at  functional  interfaces,  while  also  identifying
required actions. It should lead to-a ‘global view’ of the development process,
from a consideration of all the details.

IF QFD is introduced systematically, it should add structure to the information,
generates a framework for sensitivity analysis, and provide documentation, which
must be ‘living’ and adaptable to change. In order to understand the full impact of
QFD it is necessary to examine the changes that take place in the team and the
organization during the design and development process. The main benefit of
QFD is of course the increase in customer satisfaction, which may be measured
in terms of, for example, reductions in warranty claims.

Activity 1

Is QFD or its some variant being used in organization of your choice? Discuss
the format, if any, being used. In what ways has the concept of QFD benefitted
the organization?

........................................................................................................................

........................................................................................................................

........................................................................................................................

........................................................................................................................

8.6 RELIABILITY

Quality is a generic term meaning in conformance to requirements. When applied
to  a  hardware  product,  it  embraces  all  of  the  features  and  characteristics  of  a
product that would satisfy customers. As goods and services are often used over
a period of time, these features and characteristics need to manifest themselves
rightly and consistently over a time. The time dimension of conformance is an
important aspect of quality and this attribute is termed Reliability. The question
of reliability becomes relevant if a product fails to conform to requirements after
some period of initial conformance. Lack of reliability reflects malfunctioning of
a product or failing of a product to perform within a specified period of time. In a
fundamental way, the failures are natural in the whole universe as expressed in
the second law of Thermodynamics. Sooner or later everything decays from an
ordered state to a disordered state. Reliability is one of the important dimensions
that  have  not  been  given  as  much  emphasis  in  the  west  as  in  Japan  he  says.

189

Tools and Techniques

Uncertain performance is reflected in hesitation in buying many Indian goods
especially those manufactured by local small-scale industries, the reason being
lack of reliability of the products.

Definition and Quantification

Since ‘reliability’ denotes the chances that a product will perform over time, its
definition and quantification rely heavily upon the probability theory and statistics.
The term reliability is defined as ‘the probability of a product/entity performing
its specified functions under prescribed conditions without failure for a specified
period of time’.

An  analysis  of  this  definition  leads  to  the  following  prerequisites  for  the
quantification of reliability:

1) The quantification of reliability must be done in terms of probability.

2) The definition must specify the environment in which the product must operate

and for which reliability is quantified.

3) The  definition  must  also  include  a  statement  of  satisfactory  product

performances, that is, conformance to requirements.

4) The definition must also specify the required operating time period between

failures.

Consistent with the above definition, reliability is measured in many ways. Two
important measures are

“Mean time between failures’ (MTBF) and Failure rate per unit time. MTBF is
suitable  for  a  complete  product  that  can  be  repaired. The  product  is  operated
under specified conditions and after some time it fails to meet one of its specified
characteristics - usually a functional characteristic. The product is repaired and
operation is restarted. After a further period of time it fails again. The procedure
is continued and the times between failures are measured. The average of those
intervals is MTBF.

Failure rate is a per unit measure for a mass-produced non-repairable product,
such as electronic components.

To determine the failure rate of a population of components, say in a sample of
1000 components, a product is operated under specified conditions, and specified
functional characteristics are tested either continuously or at predetermined time
intervals. The accumulated number of failures is graphed against the product of
the number of components on test and the time on test, (this product is being
called “component hours”). The slope of this ‘survival’ curve at a particular time
gives the instantaneous failure rate of the component sample at that time. The
lower the failure rate, the better the reliability will be.

Customarily, MTBF is measured in hours and failure rate in reciprocal hours.

Reliability Engineering

190

Reliability is a design parameter just like weight, dimensions, or compressive
strength, and it can be made a part of a requirement statement, translated into

Tools and Techniques
of TQM

specifications, and submitted for verification by measurement and test. Therefore,
the basic concern is to design the product with a specified reliability and to assure
the  customer  that  the  product  does  pass  the  specified  reliability. A  discipline,
called ‘Reliability Engineering’ has been evolved over the last fifty years to deal
with these issues. This discipline essentially relates to failure statistics, testing,
prediction and improvement in reliability.

Failure  statistics  as  dominated  in  Reliability  Engineering  is  mostly  concerned
with  the  concept  of  a  probability  distribution.  Engineers  find  that  different
operating conditions and different products are better approximated by different
mathematical forms. Among the most popular are the “exponential life function”,
which is alternatively, known as the “Bathtub curve”. This is shown in the figure
8.4. The curve shows that an item may have higher possibility of failure in the
beginning phases of its use as well as after its use over a considerable length of
time. If the item is properly manufactured, it will have a little chance of failure
during its most of the useful life

Figure 8.4: Reliability Curve

Prediction, however, is only the first step. The real goal is of reliability engineering
to improve reliability and reduce failure rates over time. To accomplish these
ends, a variety of techniques are employed: “Failure mode and effect analysis
(FMEA)”, which systematically reviews the ways a product could fail and on
that  basis  proposes  alternative  designs;  individual  component  analysis,  which
computes the probability of failure of key components and then tries to eliminate
or  strengthen  the  weakest  links;  dating,  which  “  “  requires  that  parts  be  used
below their specified stress levels; and redundancy, which involves the use of a
parallel  system  to  ensure  that  backups  are  available  whenever  an  important
component or subsystem fails. An effective reliability programme also requires
close monitoring of field. Failure. Otherwise, engineers would be denied vital
information - a product’s actual operating experience - useful for planning new
designs. Field failure reporting normally involves comprehensive systems of data
collection as well as efforts to ensure that failed parts are returned to the laboratory
for further testing and analysis.

191

Tools and Techniques

Application

Reliability  normally  becomes  more  important  to  consumers  as  downtime  and
maintenance become more expensive. It is therefore a very critical dimension of
quality for consumer durable goods, capital equipment, and mission-critical items.
Unreliable products not only drive away customers but also add cost.

Though Reliability Engineering as a serious practical science grew in US defence
in  1950’s,  it  was  Japanese  industries  that  paid  serious  attention  to  the  subject
subsequently. Japanese designers always try to reduce the number of parts per
unit, following the basic principle of reliability engineering that, everything else
being  equal,  the  fewer  the  parts,  the  lower  the  failure  rates.  Parts  are  tested
rigorously. ‘Nasty tests” under varying conditions of temperature, humidity, and
voltage are conducted, as with life tests, guided by actual field data showing the
number of hours before a component typically fails. Changes in parts are often
proposed as a result. All electric and electronic components sold in Japan are
tested for reliability and the data are made available to others.

8.7

5’S’

5S occupies a prominent place as one of the basic tools to enhance the quality of
the  workplace.  In  fact,  it  forms  the  foundation  for  all  improvement  efforts  as
shown in the figure 8.5. It is an acronym for five Japanese words and denotes a
step-by-step approach for developing a clean and well-organized workplace. The
term workplace could mean shop floor, office, manager’s desk, garage, store or
any other place. It is more than housekeeping. 5S is very popular in Japan and is
becoming common in other countries too. A well-organized workplace provides
a healthy and safe work environment and also improves productivity by reducing
time for locating tools and materials, damage to the materials, etc.  A well-designed
and implemented programme of 5S would instill discipline and change the attitude
of employees toward work. It is considered one of the foundation level techniques
for continuous improvement.

Figure 8.5: Quality Improvement Pyramid

The concepts that comprise 5S activities tend to be overly didactic. This is because
the  activities  are  not  entered  on  results,  but  rather  they  emphasize  people’s
behavioural patterns, such as the elimination of unnecessary items from the work

192

environment  or  the  cleaning  and  neatening  of  equipment.  Consequently,  the
activities are of a kind that makes quantitative assessment of their effectiveness
difficult. When  5S  activities  are  promoted,  questions  are  often  raised  such  as
“which is more important, 5SS activities or work?” or “How much earnings would
5S activities bring?”

5S activities are intended to qualitatively change the ways in which people think
and behave, and, through these changes, to alter the quality of both equipment
maintenance and the work environment. Before 5S activities are begun, everyone
involved should clearly understand and codify in writing the goals and meaning
of the 5S’s for each individual organization and work environment. Furthermore,
since 5S activities must be carried out with determination and concerted effort, it
is helpful to devise slogans. Unless the specific rules are made highly pragmatic,
it  is  hard  to  put  them  into  practice.  5’S’  represents  five  action  items  that  ark
initially  done  with  some  kinds  of  persuasion.  However,  these  aspects  should
become a pan of the habit in individuals. These actions are described below:

1. SEIRI (Sort)

This denotes action to identify and sort out all items into necessary and unnecessary
items and discard all unnecessary items from the shop floor. Items include parts,
sub-assemblies, jigs, dies, raw materials, machines, files, documents in the files,
racks, rejected goods lying in the workplace or “gemba” in Japanese.

Many supervisors and shop floor managers have a tendency to keep items which
might be required in the distant future, or in greater quantities than necessary.
The number of items required for a specific timeframe should be decided. Some
of the steps comprise of

a) Classification of all items into categories - necessary (can be used in the near
future) and unnecessary (not required at all or required in the distant future).

b) Fixing the quantities of items required in the distant future to be kept in the

workplace.

c) Taking out trash and rubbish from the workplace immediately.

d) Prepare  and  circulate  a  list  of  items  which  are  not  required  to  all  other

departments/sections to identify what they can use.

e) Attaching a big red tag to all such items indicating name, disposal procedure,
and date of disposal and retention period (the period after which items will
not remain in the workplace).

f) Taking action to remove (from the workplace) dispose of these items after

the retention period,

2. SEITON (Straighten)

This is the process of arranging all necessary items in an organized manner so
that no time is lost in finding them. It involves deciding a place for everything
and keeping everything in its place. The blowing guidelines should be helpful:

a) Depending on the frequency of their use, shelf life, bulk etc., decide how and
where the item would be placed in the workplace. For example, small tools

Tools and Techniques
of TQM

193

Tools and Techniques

194

can be kept in racks while big bulky ones may be stored. More frequently
used items should be kept in the middle shelves of the racks. The principle is
to store them as near to the place of use as possible to minimize searching
and handling time.

b) Use the first-in, first-out principle to prevent loss due to deterioration.

c) Put labels on all items to clearly identify them.

d) Store dies and moulds together along with tools necessary for setting them

up.

e) Maintain a clear space around the fire extinguishers and keep passages free.

f) Clearly demarcate passages, work areas and storage areas.

g) Design  storage  methods  so  that  items  are  stocked  properly  and  are  not

damaged.

Establishing  tidiness  in  the  work  environment  depends  upon  a  study  of  work
efficiency. The amount of time needed to retrieve an item and return it to storage
should be measured and the results can then be measured on a yardstick to evaluate
the level of tidiness.

3. SEISO (Shine)

This is the process of cleaning the workplace thoroughly to remove all dust, oil,
root etc. and waste from the machines, floors, walls, and other areas. Many times,
cleaning leads to the discovery d potential Problem such are loose nuts, leakage
and war. Implementation requires three steps. These are:

• Undertaking cleaning of the workplace completely with the participation of

everybody including top and senior managers.

•

Implementing  schemes  in  your  own  machine  and  work  by  employees
responsible for the designated areas.

• Ensuring that machines and workplaces are cleaned daily.

Cleaning is more than simply cleaning up of the general environment. It also
means  guarding  from  dirt  every  single  part  of  the  item  used,  upon  which  our
livelihood depends. In other words, cleaning is a form of inspection. The problems
caused by grime, dust, and foreign matter are related to all aspects of accidents,
defects, and malfunctions. The recent tendency among young people to disdain
dirty work environments is affecting personnel recruitment.

Cleaning should not be carried out by hired contractors. Rather, it should be an
undertaking of the plant’s employees, with responsibilities assigned to everyone.
For  large  and  public  areas,  a  method  of  fair,  rotational  assignments  is
recommended. “Colour conditioning” i.e., choosing a pleasant paint scheme for
the equipment and work environment, is an important element in creating a light
and neat atmosphere. /

Personal cleanliness often refers to hygienic conditions for food and drink, such
as the facilities of hot water and tea. Recently, an increasing number of shop floor

workers  have  begun  to  wear  light-coloured  smocks.  Since  grime  and  dirt  are
readily seen on these smocks, the level of personal cleanliness can be easily judged.
These cases exemplify the goal of personal cleanliness readily apparent.

Tools and Techniques
of TQM

In  considering  the  environment  and  pollution  in  terms  of  the  people  affected,
investigation of this subject expands into several other areas, all of which should
be understood from the 5S perspective. These include dealing with oil, mist, dust,
noise,  paint-thinner-type  oil  products,  and  poisons.  Some  enterprises  promote
replacement  of  flowers  in  the  shop  environment.  Thus,  the  idea  of  personal
cleanliness embraces the upkeep of a generally clean and pleasant atmosphere.

4. SEIKETSU (Standardise)

This  means  maintaining  a  high  standard  of  workplace  organization  and
housekeeping at all times by repeating Seiri, Seiton and Seiso regularly. It involves
the following:

a) Decide a schedule specifying frequency and persons responsible for carrying
out  Seiri,  Seiton  and  Seiso  and  ensuring  that  it  is  done  according  to  the
schedule. Make 5S a routine.

b) Eliminate activities that make the workplace dirty and disorganized.

c) Protect workers from dangerous and unsafe conditions.

d) Standardize operations and daily maintenance procedures.

e)

Institute  competition  between  various  sections  departments  for  the  best
organized and maintained workplace - lay down criteria and determine the
level of 5S activities in various workplaces.

f) Managers should take note of the status in their visits to the workplace.

iv) SHITSUKE (Sustain)

This  denotes  the  self-discipline  acquired  by  practicing  4Ss  continuously,
spontaneously  and  willingly  to  make  them  a  part  of  daily  life.  It  involves
establishing standards, educating and training employees to observe good work
habits and obey the rules of the workplace.

The three pillars of 5 ‘s’

Many think that 5 ‘S’ is a working philosophy. There are three pillars on which its
implementation is dependent upon.

The first pillar to be focused upon is the disciplined work environment. The purpose
of this goal is to focus on raising the basic management level through 5S practices.
It can be seen as the essence of the 55’s themselves. 5S activities must transform
the  quality  of  human  behavior.  In  a  nutshell,  the  goal  is  to  see  that  everyone
abides by the rules once these rules are defined. Thus, of central importance are
the  ways  in  which  everyone  goes  about  carrying  out  his  or  her  duties  and
participates in activities. Of equal importance are the training methods that allow
each individual worker to be responsible for his or her assigned activities and
behavior. Improvements clearly need to be made in the area of management by
observation.

195

Tools and Techniques

196

The key to the next step - making a clean work environment - is to clean the
smallest elements of the work environment and equipment that have either never
been  cleaned  or  have  never  been  thoroughly  cleaned  and  to  get  rid  of  all  the
grime  and  dust.  By  thus  radically  transforming  the  condition  of  the  work
environment,  the  workers  will  be  both  motivated  and  inspired  to  renewed
awareness and behaviour.

The third pillar of 5S is the creation of a work environment that can be managed
by  seeing,  an  idea  popularly  referred  to  as  management  by  observation.  By
improving  upon  ways  to  identify  abnormal  conditions  quickly  and  easily,  it
becomes  possible  to  create  an  environment  in  which  anyone  in  an  area  can
spontaneously help someone else when an abnormal condition occurs. This means
that measures are taken to prevent people from making mistakes and committing
errors, and can be called the standardization of the 5Ss.

These activities that comprise the three pillars should be pursued simultaneously
to take advantage of the mutual interrelationship among them.

Activity 2

Choose an organization which uses the concept of 5S. Prepare a  table of the
activities performed by the organization using 5S.

........................................................................................................................

........................................................................................................................

........................................................................................................................

........................................................................................................................

8.8 ZERO DEFECTS (ZD)

There are numerous people engaged in a large number of activities related to
marketing,  design,  manufacturing,  distribution,  etc.  who  contribute  to  make  a
product. If a product has to meet requirements of a customer, necessary instruction
for every person involved requires description of every aspect of the product in
precise, standardized and commonly understandable terms. These terms are known
as  specifications. Any  variation  that  is  caused  while  translating  customers’
requirements into right specifications or while producing needed specifications
is considered as a defect. Unless special care is taken, such variations are normal.

Many people believe that it is uneconomical to eliminate all kinds of variations -
major and minor ones -that are thought to normally happen at every work step. It
is precisely the reason that acceptable quality level. (AQL) in statistical Quality
Control has been used to define quality of goods and services in transactions.

A defect in missile could therefore be fixed, although it was likely to require
extensive debugging before shipment. Subsequently, Martin’s general manager
accepted a request from the U.S. Army’s missile command to deliver the missile
one month ahead of schedule. He went even further - he promised that the missile
would  be  perfect,  with  no  hardware  problems,  no  document  errors,  and  all
equipment  set  up  and  fully  operational  ten  days  after  delivery  (the  norm  was
ninety days or more). Two months of feverish activity followed. Since little time

was available for the usual inspection and after-the-fact correction of errors, all
employees were asked to contribute to building the missile exactly right the first
time. The result was still a surprise; a perfect missile was delivered. It arrived on
time and was fully operational in less than twenty-four hours.

This experience was an eye-opener for Martin. After careful review management
it was concluded that the project’s success was primarily a reflection of its own
changed  attitude.  The  reason  behind  the  lack  of  perfection  was  simply  that
perfection  had  not  been  expected.  Once  management  demanded  perfection,  it
happened! Similar reasoning suggested a need to focus on workers’ motivation
and  awareness.  Of  the  three  most  common  causes  of  worker  errors  -  lack  of
knowledge, lack of proper facilities, and lack of attention management concluded
that  the  last  had  been  least  often  addressed.  It  set  out  to  design  a  programme
whose overriding goal was to “promote a constant, conscious desire to do a job
(any job) right the first time”. The resulting programme was called zero defects.

Operating Principle

Crosby argues that if management is serious about achieving ZD, it has to be
serious about prevention. He proposes some guidelines for managers which he
calls the ‘four absolutes of quality management’. These should be reflected in
their attitude and management systems:

a) Quality  means  conformance  to  the  requirements:  The  setting  of
requirements is management responsibility as are the communication devices
and their effectiveness. Crosby argues that if management wants people to
do things right the first time, they have to tell everyone clearly what that is;
this must be expressed in objective terms as much as possible.

b) Quality comes from prevention: The first absolute was to understand the
process  by  which  various  processes  are  involved  in  producing  products/
services. The second is about identifying and eliminating all chances for an
error to occur; this requires meticulous observation and analysis.

c) Quality performance standard is Zero Defects: This is conformance to
the requirements and should be the personal performance standard of everyone
in  the  organization  according  to  Crosby,  and  will  come  from  a  change  in
attitudes; everybody needs to believe that it is always cheaper to do the job
right the first time.

d) Quality measurement is the price of non-conformance ie. cost of quality:
According to Crosby, manufacturing organizations spend 25% of sales doing
things wrong and service organizations spend about 40% of their operating
costs on the same wasteful actions.

Approach For ZD Implementation

To achieve great improvements, the management has to believe in the following:

• The  conviction  by  senior  managers  that  they  have  had  enough  of  quality
being a problem and wanting to turn it into an asset; pursuit of ZD will improve
skill and knowledge of workers and managers.

• The commitment that they will understand and implement the four absolutes

of quality management;

Tools and Techniques
of TQM

197

Tools and Techniques

• The conversion to that way of thinking from the conventional wisdom that

caused the problem in the first place.

Crosby argues that it takes a long time to transfer from conviction to conversion
but that as soon as the transfer process begins, it is a positive sign that improvement
has started to take place.

The Crosby approach to total quality is to change the culture and attitudes within
an organization to implement continuous improvement. This approach is therefore
more management - oriented than tool -oriented since it does not refer at all to the
control of quality by the use of various statistical techniques. He has developed a
management  maturity  grid  based  on  management  attitude  to  quality  and  the
progression of quality performance achievements. An abridged version of above
mentioned Quality Management Maturity

Grid is given in the Table 8.1. Crosby has suggested a 14- step quality improvement
approach to reach the good of ZD. These steps are as follows:

i. Management  commitment:  Management  should  commit  itself  to
participating in a quality improvement programme. Quality improvement
never happens automatically but must be planned and managed.

ii. Quality improvement team: Representatives of each department should
form a team. Its responsibilities embrace the whole quality improvement
programme of the organization.

iii. Quality  measurement:  Determine  the  status  of  quality  throughout  the
organization.  Most  quality  improvement  programmes  depend  on  the
systematic accumulation and analysis of quantitative data.

iv. Cost of quality evaluation: Establish the cost of quality to indicate where

corrective action will be profitable for the organization.

v.

Quality awareness: Share with employees the measurements of what non-
quality is costing through training and communication material.

vi. Corrective action: Bring problems to light for all to see and resolve them
on  a  regular  basis  where  possible.  It  is  for  the  supervisors  to  work  out
solutions.

vii. Establish an ad hoc committee for the Zero Defects programme: After
a year has gone by, the observance of a Zero Defects Day will be organization
management’s  commitment  to  ‘Zero  Defects’  and  also  the  thought  that
everyone should do things right the first time.

viii. Supervisor training: A formal orientation of the Zero Defects programme
with  all  levels  of  management  should  be  conducted  prior  to  its
implementation.

ix. Zero  Defects  Day:  Zero  Defects  as  the  performance  standard  of  the
organization  is  observed  on  a  day  to  provide  emphasis  and  long  lasting
impression.

x.

Goal setting: Regular meetings between supervisors and employees help

198

people think in terms of meeting goal and accomplishing specific tasks as a
team.

Tools and Techniques
of TQM

d
i
r
G
y
t
i
r
u
t
a
M

t
n
e
m
e
g
a
n
a
M
y
t
i
l
a
u
Q

:
1
.
8

e
l

b
a
T

xi. Removal of error causes: Individuals are asked to describe any problems
that keep them from performing error-free work. The appropriate functional
group will develop an answer to those problems.

199

Tools and Techniques

xii. Recognition: Award programmes are established to recognise those who
meet their goals or perform outstanding acts. Awards need not be financial,
recognition is what is important.

xiii. Quality councils: Quality professionals and team chairpersons should meet
regularly to communicate and determine actions to upgrade and improve
the quality improvement programme.

xiv. Do  it  again:  Set  up  a  new  team  of  representatives  and  begin  again  to
overcome the turnover and changing situations that can occur in the year to
18 months to implement the typical quality improvement programme.

The above-mentioned quality improvement philosophy has found its application
all over the, world in many industries like Automobile, Medicine, Defense, etc. It
requires sustained efforts on the part of management.

8.9 RE-ENGINEERING

Concept

It was only during 1980’s western management got convinced to the effect that a
process i.e. a planned set of actions effect product quality considerably as shown
in Figure 9.5. A process converts inputs to outputs with the help of transforming
resources. Unless proper resources, and inputs are properly acted upon, output
quality leading to customer satisfaction could not be achieved. Such processes
could be visualized at different levels - Business Process, Functional Process,
Work Process, etc. depending upon the span of work. Business Process links up
organizational activities to deliver specified set of goods and services to a customer.
Hence, considerable amount of efforts are now made to improve upon such a
business process in order to improve quality. Information Technology has been
extensively used to modify a business process so as to deliver required services
to customers. Often major modification is required to be made so as to ensure
delivery of quality goods and services. Such major change to a business process
is termed as Business Process Re-Engineering.

Figure 8.6: Process Concept for Quality

According to Hammer and Champy, Business Process Reengineering (BPR) is
the fundamental rethinking and radical redesign of business processes to achieve
dramatic improvements in critical and contemporary measures of performance,
such as cost, quality, services and speed .

200

The above definition which is accepted by all could be elaborated further if the
four key components of the definition are explained to a greater extent in the
light of the understanding which western countries have built up over the years
as given below:

a) Fundamental rethinking and radical redesign signifies an innovation that is
a new way of thinking and acting. Fundamental rethinking refers to an enquiry
on the most basic thing and asking fundamental questions about the existing
methods and prevailing practices in organizations. Thus, one gets to the root of
the things: not making superficial changes or refinements with what is already
in place. People who are conversant with work study remember the purpose of
asking a basic question -’WHY?’ Finding an answer related to the fundamental
reason for an action helps one make a breakthrough improvement.

b) Business process is a sequence of activities or operations performed on one
or  more  inputs  to  deliver  an  output.  It  is  a  customer/demand  driven,
technologically ordered set of operations. For example, an order fulfillment
process includes several tasks which are required to be carried out by different
functional departments of an organization. Such cross-functional set of tasks
is often the focus for BPR.

c) Dramatic improvement reflects achievements in terms of customer valued
performance measures. It implies not to be content just with 10 or 20 per cent
improvement in a certain activity or process but to get 10 times improvement
and so on.

d) Critical and contemporary measures of performance highlight the criteria
which dominant stakeholders in the prevailing markets look for. This includes
an assessment of the bargaining strength of various stakeholders as well as
the priorities in their expectations. This part of the definition makes BPR a
dynamic and context-dependent contingency management approach. There
are many other definitions provided by experts throughout the world. Most
of these definitions differ in emphasis.

Characteristics of Reengineering

The following are the common features among BPR applications as found by
Hammer and Champy .

Several jobs are combined into one

In this case one person will be doing all the tasks. Such a person will be known as
a  case  worker.  In  some  cases  it  is  not  possible  to  compress  all  the  steps  of  a
lengthy process into one integrated job performed by a single person. In those
situations, the organization may require more persons, each managing parts of a
process. Such a team will be known as a process team. In both the cases, the
worker involved should be multi-skilled as his work becomes multidimensional.

Processes have multiple versions

This  refers  to  the  end  of  standardisation.  To  meet  the  demands  of  today’s
environment, we need multiple versions of the same process, each one tuned to
the requirements of different market situations or inputs. Traditional one-size-

Tools and Techniques
of TQM

201

Tools and Techniques

fits-all processes are usually very complex, since they must incorporate special
procedures and expectations to handle a wide range of situations. A multi-version
process, by contrast, is clean and simple because each version needs to handle
only the case for which it is appropriate.

Work is performed where it is directly needed

This means that work should be shifted across the organizational boundaries, i.e.
the work should be done at the place where it is required most. Hammer cited the
example  of  purchasing  stationery  items.  When  done  by  a  central  purchasing
department, there is an inevitable delay. So, purchasing has to be done by the
user department which requires the stationary items.

Non-value adding activities are reduced

For  effective  reengineering,  checks  and  controls  should  be  minimized.
Reengineering  processes  use  controls  only  to  the  extent  they  make  economic
sense. In the reengineering environment a larger number of people are empowered,
so people become responsible for the end product.

Reengineering  organization  may  look  like  a  cent  raked  as  well  as  decent
raked system

Organizations which have reengineered their processes have the privilege to get
the advantages of centralization and decentralization in the same process mostly
on account of availability of modern IT facilities.

In fact, the above mentioned six characteristic from the basic design principles
for BPR.

Methodology

There is a wide range of methodology through which an organization seeks to
synergise some of the ideas implicit in the reengineering concept. While some
methods focus on the analysis and redesign tasks, others focus on the definition
of strategy or the development of the underling information system.

Given the wide variety of methods in practice, a typical one developed by Talwar
(1994) is outlined below.

This methodology seeks to strike a balance between strategy formulation, process
redesign, and exploitation and management of the reengineered business. It entails
three stages below.

• Programmeme Initiation: Objectives and scope for the study are delineated.

• Design  and  implementation:  Processes  as  decided  under  the  scope  are

redesigned and prototypes are formulated.

• Exploitation of the re-engineered business: The redesigned processes and

changes it enables are implemented.

Programme Initiation

202

• Build the awareness of business processes, create an understanding of the
concepts  of  reengineering  and,  generate  an  interest  in  the  need  for,  and
opportunities to achieve sustainable performance improvement.

• Clarify the strategic direction and target architecture. Determine the strategic
objectives for the exercise. Decide on the scale of change required and the
number and scope of the candidate processes for reengineering. Define the
business  requirements  and  performance  objectives  that  the  re-engineered
processes will fulfill and select a programmeme owner and project teams (s).

• Undertake the detailed planning of the change process.

In  short,  the  first  stage  prepares  the  ground  for  undertaking  a  reengineering
exercise.

Design & Implementation

• Map,  model  and  analyse  the  current  process  (es),  capturing  performance
measures to help highlight the need for change and determine if immediate
improvement  can  be  made.  Identify  the  customer  requirements  and
expectations  from  the  process  and  (possibly)  benchmark  the  process.  In
analyzing a process it is important to distinguish between the flows of activity
and control in the process and the ways in which data and documents are
used in the process.

• Generate a range of options for redesigning the process, each of which will
significantly improve performance,typically using different configurations
of process roles, work tasks and technology support.

• Test the options against key measures, such as customer requirement, cost
and quality objectives. Select the preferred option and develop the business
case. Develop the redesigned business process (es), develop or enhance the
underlying computer systems add plan the migration steps.

•

Prototype, test and refine the redesign in a laboratory setting; train the users
and integrate the reengineered processes into the live business environment;
test them in operation and implement any immediate refinements.

Thus, the stage undertakes all the technical aspects of reengineering.

Exploitation of the Reengineered Business

•

Provide ongoing support to the reengineering operations, help managers and
staff adjust to new roles, responsibilities and methods of working; monitor
performance an’d initiate ongoing refinements.

• Ensure  a  continuous  review  of  the  opportunities  to  exploit  the  enhanced

capabilities created through reengineering.

• Maintain  a  balance  between  continuous  incremental  improvements  and

periodic fundamental changes in process design.

The last stage is thus concerned with implementation and periodical review.

Application

A  developing  country  like  India  offers  vast  scope  for  application  of  BPR  as
organizational capabilities in most sectors required for the market economy do
not quite match the competitive demands. Most organizations which have hitherto

Tools and Techniques
of TQM

203

Tools and Techniques

204

been operating under a protected environment are predominantly bureaucratic in
structure and style, and operating systems consist of age-old clerical operations
carried out in sequential desk-to-desk manner. Rising competition is expected to
force organizations to change all this.

Severe competition makes an organization customer-driven. A thorough study of
the market and the strategic capability of an organization is therefore essential to
pinpoint the areas requiring priority actions for changes.

BPR involves changes in organization structure, roles and responsibilities, rewards
and  recognition  systems,  etc.  Such  changes  pose  great  challenges  to  Indian
organizations. However, given the perceived threat and eagerness to change the
age-old work practices, especially in the emergent liberalised economic situation,
coupled with the entry of multinationals in many sectors, Indian management is
believed to be willing to adopt BPR. With the rise in the educational level of
future employees, and a variety of IT hardware -and software on offer, BPR may
become  a  preferred  choice  for  Indian  management  for  effecting  a  strategic
breakthrough.

Activity 3

Is your organization or any other organization you know of or familiar with
have  any  of  the  five  Concepts/approaches  discussed  in  this  unit  viz.,
Reliability, Off-line quality control, 5S, Zero defects, and Reengineering.
Have any of these concepts/ideas/approaches been applied? Discuss the state
of the art, as it exists in the organization concerned, highlighting the salient
features  of  each  and  the  benefits  the  organization  has  derived  from  its
application.

............................................................................................................................

............................................................................................................................

............................................................................................................................

............................................................................................................................

8.10 TAGUCHI METHODS

In this section we discuss briefly the methods that belong to the domain of quality
engineering, a recently formalized discipline that aims at developing products
whose superior performance delights only when the package is opened, but also
throughout their lifetime of use. The quality of such products is robust, i.e., it
remains unaffected by the deleterious impact of environmental or other factors
often beyond the users’ control.

Since  the  topic  of  quality  engineering  is  of  notably  broad  appeal,  we  include
below a brief review of the associated rationale and methods. The term “quality
engineering” (QE) was used till recently by Japanese quality experts only. One
such expert is Genichi Taguchi (1986) who reasoned that even the best available
manufacturing technology was by itself no assurance that the final product would
actually  function  in  the  hands  of  its  user  as  desired.  To  achieve  this  Taguchi
suggested  the  designer  must  “engineer”  quality  into  the  product,  just  as  s/he

specifies the product’s physical dimensions to make the dimensions of the final
product correct.

Tools and Techniques
of TQM

QE  requires  systematic  experimentation  with  carefully  developed  prototypes
whose performance is tested in actual field conditions. The object is to discover
the optimum set-point values of the different design parameters, to ensure that
the final product would perform as expected consistent in actual use. A quality-
engineered product has robust performance.

Taguchi’s Thoughts on Quality

Taguchi, a Japanese electrical engineer by training, is credited to have made several
contributions in the management and assurance of quality. Taguchi studied the
methods of design of experiments (DOE) at the Indian Statistical Institute in the
1950s and later applied these methods in a very creative manner to improve product
and process design. His methods now form the foundation of engineering design
methodology  in  many  leading  industries  around  the  world,  including AT&T,
General Motors and IBM.

Taguchi’s contributions may be classified under the following three headings:

• The loss function

• Robust design of products and production processes

• Simplified industrial statistical experiments

The essence of the loss function concept may be stated as follows. Whenever a
product deviates from its target performance, it generates a loss to society. This
loss is minimum when performance is right on target, but it grows gradually as
one deviates from the target. Such a philosophy suggests that the traditional “if it
is within specs, the product is good with a view of judging a product’s quality is
not correct”.

If  your  foot  size  is  7,  then  a  shoe  of  size  different  front  7  will  cause  you
inconvenience, pain, loose fit, and even embarrassment. Under such conditions it
is meaningless to seek a shoe that meets a spec given as (7 + x).

To  state  again,  the  loss  function  philosophy  says  that  for  a  producer,  the  best
strategy is to produce products as close to the target as possible, rather than aiming
at “being within specifications.”

The other contributions of Taguchi are a methodology to minimize performance
or quality problems arising due to non-ideal operating or environmental conditions,
and a simplified method known as orthogonal array experiments to help conduct
multi-factor experiments toward seeking the best product or process design. These
ideas may be described as follows.

The Secret of Creating a Robust Design

A practice common in traditional engineering design is sensitivity analysis. For
instance, in traditional electronic circuit design, as well as the development of
performance design equations, sensitivity analysis of the circuit developed remains
a key step that the designer must complete before her/his job is over.

205

Tools and Techniques

206

Sensitivity  analysis  evaluates  the  likely  changes  in  the  device’s  performance,
usually due to element value tolerances or due to value changes with time and
temperature.

Sensitivity analysis also determines the changes to be expected in the design’s
performance due to factor variations of uncontrollable character. If the design is
found to be too sensitive, the designer projects the worst-case scenario to help
plan for the unexpected. However, studies indicate that worst-case projections or
conservative designs are often unnecessary and that a “robust design can greatly
reduce  off  target  performance  caused  by  poorly  controlled  manufacturing
conditions,  temperature  or  humidity  shifts,  wider  component  tolerances  used
during fabrication, and also field abuse that might occur due to voltage frequency
fluctuations, vibration, etc.

Robust design should not be confused with rugged or conservative design, which
adds to unit cost by using heavier insulation or high reliability, high tolerance
components. As an engineering methodology robust design seeks to reduce the
sensitivity of the product process performance to the uncontrolled factors sthrough
a careful selection of the values of the design parameters. One straightforward
”
way to produce robust designs is to apply the “Taguchi method .

Robust Design by the “Two-step” Taguchi Method

Note that a product’s performance is “fixed” primarily by its design, i.e.,by the
settings selected for its various design factors. Performance may also be affected
by noise/environmental factors, unit to unit variation in material, workmanship,
methods, etc., or due to aging/deterioration. The breakthrough in product design
that Taguchi achieved renders performance robust even in the presence of noise,
without actually controlling the noise factors themselves. Taguchi’s special “design
‘noise array ‘experiments discover those optimum settings. Briefly, the procedure
first builds a special assortment of prototype designs -(as guided by the “design
array”) and then tests these prototypes for their robustness in “noisy” conditions.
For this, each prototype is “shaken” by deliberately subjecting it to different levels
of noise (selected from the “noise array”, which simulates noise variation in field
conditions).Thus performance is studied systematically under noise in order to
find eventually a design that is insensitive to the influence of noise.

To guide the discovery the “optimum” design factor settings Taguchi suggested a
two-step procedure. In Step 1, optimum settings for certain design factors (called
“robustness seeking factors”) are sought so as to ensure that the response (for the
bar, plasticity) becomes robust (i.e., the bar does not collapse into a blob at least
up to 50°C temperature). In Step 2, the optimum setting of some other design
factor (called the adjustment” factor) is sought to put the design’s average response
at the desired target (e.g., for a plasticity level that is easily chewable).

Taguchi Orthogonal May Experiment

Rather  typically,  the  performance  of  a  product  (or  process)  is  affected  by  a
multitude of factors. It is also well-known that over 213 of all product malfunctions
may be traced to the design of the product. To the extent basic scientific knowledge
allows the designer to guide his/her design, the designer does her/his  to come up
with selection of design parameter values that would ensure good performance.

Frequently though, not everything can be predicted by theory and experimentation
or prototyping must be resorted to and the design must be empirically optimized.
The  planning  of  such  experimental  multiple  factor  investigations  falls  in  the
domain of statistical design of experiments (DOE).

Tools and Techniques
of TQM

Quality Control by Taguchi’s Method

A typical quality system of a manufacturing organization consisting of three
aspects - quality of design, quality of conformance, and quality of service -
could be broken down into two parts as follows:

• Off-line Quality Control (QC): Activities for quality of design through
market research and Product/process development, which are QC efforts
away from production lines.

• On-line Quality Control (QC): Activities for quality of conformance and
quality of service through manufacturing care, inspection and customer
service.  These  are  QC  efforts  mainly  on  production  lines.  Reliability
Engineering as explained in an earlier section is one way of off-line quality
control activity.

One of the well-known Japanese quality gurus, Genichi Taguchi, has drawn
attention to another off-line quality control activity that aims at developing
an optimum set of product and process conditions that would produce more
uniform goods and services. According to him, any deviation from a target
value of a critical dimension would cause a loss either to the producer or to
consumer  i.e.  to  society.  He  strongly  recommends  close  uniformity  among
parts, components and products so as to cause minimum loss to a society. His
major focus has therefore been on the design stage.

Principles and Methods

According to Taguchi, designing should consist of the following three activities

a)

b)

c)

System design.

Parameter design

Tolerance design

The method starts up with system-design reasoning. This involves both product
design and Product design.

Product design induces choice of materials and parts, and includes the calculating
starting figures for product levels. Process design induces choice of equipment
and taking a first shot at deriving process factor levels. Next, the method calls for
parameter design. The aim is to find, from the start points already determined, an
optimal mix of product parameter levels and process operating levels. Emphasis
is  placed  on  sensitivity  to  environmental  perturbations  and  anything  else  that
cannot  normally  be  dealt  with  using  control  procedures  of  the  organization.
Reducing sensitivity is the aim. Securing minimum sensitivity relies on the help
of techniques. Taguchi’s techniques include ones that are efficient in searching
for the optimal, workable, survival mix. Tolerance design then builds in tolerance
to factors that can significantly affect the variations of the product. This might

207

Tools and Techniques

mean investment of money to improve equipment and materials. Tolerance design
concludes with prototyping.

Once prototyping is complete, implementation is undertaken. At this stage use of
Statistical Quality Control (SQC) would be relevant. Quality in design and process
control clearly follow on.

‘Robust design’ uses the following statistical design optimization tools:

• Matrix Experiment
• Analysis of Mean (ANOM)
• Analysis of Variance (ANOVA)
•

Signal-to-Noise (SIN) Ratios.

a) Matrix Experiment: It is the minimum set of experiments which are required
to be performed with combinations of different levels of control factors (design
parameters)  so  that  it  is  possible  through  data  analysis  to  predict  the  best
combination  of  the  control  factors  which  make  the  variance  due  to  noise
factors  a  minimum. The  matrix  experiment  is  based  on  orthogonal  arrays
taken from linear algebra.

b) Analysis  of  Mean  (ANOM):  It  is  a  data  analysis  method  which  helps  to
estimate the contribution of each level of every control factor to the Signal-
to-Noise ratios. With the help of ANOM it is possible to predict the optimum
combination of control factor levels to get quality-cost optimization.

c) Analysis of variance (ANOVA): It is a data analysis method which help to
estimate the strength of each control factor relative to other in influencing
variation in the Signal-Noise Ratio (variance).

d) Signal-to-Noise (SIN) Ratio: It is a new measure of quality as seen from the

customer point of view.

The  SIN  Ratios  were  first  proposed  by  Taguchi  and  form  the  basis  for  the
improvement  in  quality  purely  through  experiments.  Maximising  SIN  ratio  is
equivalent to reducing variance due to various noise factors and hence improves
quality  during  manufacturing,  customer  usage  and  aging  and  simultaneously
reducing cost substantially.

Robust Design aims at finding, through structured experiments and data analysis,
the combination of design parameters which give a maximum value of SIN ratios.

Strengths and Weaknesses of Taguchi’s Method

The main strengths are:

• Taguchi’s  method  pulls  quality  right  back  into  the  design  stage  rather
than relying on adjustments to the process on-line, or inspection of the
final product.

• The  philosophy  recognises  quality  as  a  societal  issue  and  not  just  an
organizational one. Quality is the minimum loss imparted by the product
to society from the time the product is shipped.

208

• The  method  is  developed  for  practicing  engineers  rather  than  theoretical

statisticians.

Tools and Techniques
of TQM

• The method helps an organization to determine the best method of process
control,  reducing  process  costs  incurring  only  small  amounts  of  capital
expenditure.

• The main weaknesses are:

 The method has little relevance to processes where measurement does
not produce data that can be accessed through sensitivity analysis and
minimization; i-e., it is not relevant to many important success factors in
the service sector.

 There  are  no  directives  about  how  to  manage  a  quality-oriented
organization, particularly the people. Quality is placed organizationally
in the hands of a specialised team of expert designers and does not involve
managers and workers. Taguchi’s method is designed for engineers and
not managers.

 Taguchi has nothing to say about humans as social, cultural or political
beings and therefore makes no contribution to managing employees.

Inspite of many limitations, Taguchi method is finding increasing applications.

Applications

Every application of Robust Design has given incredible results. The following
are  the  few  examples  of  its  application  mostly  in  U.S.A  which  indicate  the
incredible power of this method for improving quality and reducing costs.

(ii) Window Photolithography

This was the first application in the USA that demonstrated the power of th-e
Robust Design approach to quality cost optimization. The benefits achieved were

•

•

•

4 fold reduction in process variance

3 fold reduction in fatal defect

2 fold reduction in process time

• Easy transition - design to manufacturing:

(iii)  Polysilicon Deposition Process

This process is one of the important steps in the manufacturer of very large scale
integrated (VLSI) circuit. The existing process gives as high as 5000 defects per
units’ surface area of the silicon wafers. In all, 6 design parameters like furnace
temperature,  gas  flow,  gas  pressure,  settling  time  and  cleaning  method,  were
investigated  with  18  experiments.  The  project  was  completed  in  9  days.  The
benefits were

•

Surface defect count was consistently reduced to less than 10 defects per unit
surface area

209

Tools and Techniques

• Yield improved manifold

• One expensive on-line inspection position was completely removed.

iv)  Drilling a Hole in Cast Alloy Wheel

The existing drilling process gave heavy rejection of cast alloy wheels of racing
cars due to high variance in the diameter of drilled hole in the wheel for installing
the air valve stem. The benefits were

•

diameter variation Gas reduced by 70%

• US 60000 dollars were saved.

There are a large number of applications in U.S., Europe & Japan, as above that
could be illustrated. A few organizations in India, who have seriously tried to
apply Robust Design, have obtained very encouraging results in their first trial
applications. These organizations mostly belong to the Telecommunication sector.

8.11 SIX SIGMA PRINCIPLE

The six sigma principle is Motorola’s own rendering of what is known in the
quality literature as the zero facts (ZD) programme. Zero defects is a philosophical
benchmark or standard of excellence in quality proposed by Philip Crosby. Crosby
explained the mission and essence of ZD by the statement. What standard would
you  set  on  how  many  babies  nurses  are  allowed  to  drop?”  ZD  is  aimed  at
stimulating  each  employee  to  care  about  accuracy  and  completeness,  to  pay
attention to detail, and to improve work habits. By adopting this mind-set, everyone
assumes the responsibility toward reducing his or her own errors to zero.

One might think that having three-sigma quality, i.e., the natural variability equal
to tolerance (= upper spec limit - lower spec limit, or in other words, Cp = 1.0)
would mean good enough quality. After all, if distribution is normal, only 0.27%
of the output would be expected to fall outside the product’s specs or tolerance
range. But what does this really mean? An average aircraft consists of 10,000
different  parts. At  3-sigma  quality,  27  of  those  parts  in  an  assembled  aircraft
would be defective. At this performance level, there would be no electricity or
water in Delhi for one full day each year. Even four sigma quality may not be
OK. At four-sigma level there would be 62.10 minutes of telephone shut down
every week.

You might wish to know where performance is today. Restaurant bill errors are
near 3-sigma. Payroll processing errors are near 4-sigma. Wire transfer of funds
in banks is near 4-sigma and so is baggage mishandling by airlines. The average
Indian manufacturing industry is near the 3-sigma level. Airline flight fatality
rates are at about 6.5 sigma level (0.25 per million landings). At two-sigma level
an organization’s cost of returns, scrap, rework and erosion of market share costs
over a third of its yearly sales.

For the typical Indian, a 1-hour train delay, an incorrect eye operation or drug
administration, or no electricity or water half a day is no surprise; helter routinely
experiences even worse performance. Quantitatively, such performance is worse
than two-sigma. Can this be called acceptable? One- or two sigma performance

210

is downright noncompetitive.

Tools and Techniques
of TQM

Besides  adopting  TQM  as  the  way  to  conduct  business,  many  organizations
worldwide are now seriously looking at six-sigma benchmarks to assess where
they stand. Six sigma not only reduces defects and raises customer acceptability;
it has been now shown that it can actually save money as well.

The Step to Six Sigma

Motorola prescribes six steps to achieve the six-sigma state, as follows.

Step 1 :

Identify the product you create or service you provide.

Step 2 :

Step 3 :

Identify the customer(s) for your product or service and determine
what they consider important.

identify your needs to provide the product or service that satisfies the
customer.

Step 4 : Define the process for doing the work.

Step 5 : Mistake-proof the process and eliminate waste effort.

Step 6 :

Ensure  continuous  improvement  by  measuring,  analyzing  and
controlling the improved process.

Many organizations have adopted the Measure-Analyze-Improve-Control cycle
to step into six sigma.

Typically they proceed as follows:

•

Select critical-to-quality characteristics

• Define performance standards (the targets to be achieved)

• Validate measurement systems (to ensure that the data is reliable)

• Establish Product Capability (how good are you now?)

• Define performance objectives

•

•

•

Identify sources of variation (seven tools etc.)

Screen potential causes (correlation studies, etc.)

Statistical Quality Control

• Discover  relationship  between  variables  causes  or  factors  and  the  output

(DOE)

• Establish operating tolerances for input factors and output variables

• Validate the measurement system

• Determine Process Capability (CPK) (Can you deliver? What do you need to

improve?)

•

Implement process controls

One must audit and review nonstop to ensure that one is moving along the charted
path.

211

Tools and Techniques

212

The  aspect  common  between  six    sigma  and  ZD  (“zero  defects”)  is  that  both
concepts require the maximum participation by-the entire organization. In other
words, they require that unrelenting effort by management and the involvement
of all employees. Organizations such as General Motors have used a four-phase
approach to seek six sigma. These are:

1. Measure:  Select  critical  quality  characteristics  though  Pareto  charts;
determine  the  existing  frequency  of  defects,  define  target  performance
standard, validate the measurements system and establish existing process
capability.

2. Analyze:  Understand  when,  where,  and  why  defects  occur  by  defining

performance objectives and sources of variation.

3.

Improve: Identify potential causes, discover cause-effect relationships, and
establish operating tolerances.

4. Control:  Maintain  improvements  by  validating  the  measurement  system,
determining process capability, and implementing process control systems.

8.12 CROSS FUNCTIONAL MANAGEMENT

Hierarchical organizations are designed to manage the vertical flow of tasks. The
horizontal flow between departments is managed through “co-ordination” efforts
of managers who handle multiple departments and through meetings, committees
or task forces. None of these structures has ever worked altogether satisfactorily,
and therefore many attempts have been made to reform this structure.

The basic problems are two-fold. One, the processes by which work gets done in
the  organizations  are  horizontal,  that  is,  cross-departmental. Almost  anything
worthwhile  in  an  organization  need  to  move  through  multiple  departments  or
sections. Cost, Delivery, Safety and Morale (Q,C,D,S and M) require horizontal
or cross-departmental management.

The first to see the real business organization as horizontal rather than vertical
was Deming who in 1950, sketched out what he called the organization structure.
Though the processes flow horizontally, the structure of an organization can turn
into  what  has  been  described  as  functional,  where  departments  can  become
fortresses defending their positions and thus interfering with the primary task of
satisfying customers.

In Japan, the challenge of cross-functional management was first taken by Toyota
with the help of Ishikawa. The result was what is called in TQM as cross-functional
management. For example, Toyota viewed the functions of assuring quality and
control of costs.

The horizontal parts to an otherwise vertical set of parts enables the organization
to be knit into a fabric instead of being loose strings. The horizontal integration is
enabled by cross-functional committees which comprise of five or six members
of  top  management,  for  each  committee.  The  committee  is  responsible  for
establishing  directions  and  policies  for  the  function  (eg.,  quality).  It  does  not
concern itself with the day to day management.

In the 1990s, Business Process Reengineering (BPR), a method evolved in the
U.S.  for  overthrowing  deficient  processes  an  replacing  them  with  efficient
processes meets customer requirements more effectively has gained ground. BPR
works closely with an advanced use of information technology. BPR has also
emphasized the fact that processes are horizontal while organizations tend to be
vertical. It has attempted to break the vertical structure down and replace it with
horizontal  designs.  Such  structures  are  called  process  based  or  team-based
organizations.  They  enable  the  jobs  of  individuals  to  be  enriched  across
departments,  and  clarify  the  flow  of  the  processes  towards  the  satisfaction  of
customers.  This  brings  about  job  satisfaction.  Cross  functional  management,
Japanese style, will still need to be applied in order to integrate the functions of
Q,C,D,S  and  M,  but  then  the  processes  themselves  manage  Q,C,  D,S,M  in  a
more integrate the manner.

8.13 HYPOTHESIS

A hypothesis is a statement or proposition that is formulated to explain a certain
phenomenon or set of observations. It is an educated guess or prediction about
the relationship between variables that can be tested through empirical research.

In  scientific  research,  hypotheses  are  used  to  guide  the  research  process  by
providing a framework for collecting and analyzing data. Hypotheses can be either
directional, which predict the direction of the relationship between variables (e.g.,
“increasing X will lead to an increase in Y”), or non-directional, which predict
the existence of a relationship between variables (e.g., “there is a relationship
between X and Y”).

Once a hypothesis has been formulated, researchers can then design experiments
or studies to test the hypothesis. The results of these experiments can either support
or reject the hypothesis, which can then be used to refine the hypothesis or to
develop new hypotheses for further research.

Hypothesis in TQM

In Total Quality Management (TQM), a hypothesis is a proposed explanation for
a problem or challenge that a business is facing. The hypothesis is used to guide
the development of solutions and to determine the effectiveness of those solutions
through data analysis and testing.

TQM  involves  a  continuous  improvement  process,  where  the  organization
identifies  areas  for  improvement  and  uses  data-driven  analysis  to  develop
solutions. The hypothesis helps to focus this process by identifying the potential
causes of the problem and suggesting a solution that can be tested.

For example, if an organization is experiencing a high rate of defects in their
products,  a  hypothesis  might  be  that  the  defects  are  caused  by  a  particular
manufacturing process. The organization can then test this hypothesis by collecting
data on the manufacturing process and analyzing it to determine whether there is
a correlation between the process and the defects.

Tools and Techniques
of TQM

213

Tools and Techniques

214

If  the  data  supports  the  hypothesis,  the  organization  can  then  develop  and
implement solutions to improve the manufacturing process and reduce the rate of
defects. If the data does not support the hypothesis, the organization can refine
the hypothesis or develop a new one to guide further investigation.

The  use  of  hypotheses  in  TQM  helps  organizations  to  focus  their  efforts  on
identifying and solving the root causes of problems, rather than just treating the
symptoms.

Some examples of hypotheses that could be used in Total Quality Management
(TQM) are listed below:

Hypothesis : The high defect rate in a product is due to a problem with the
manufacturing process. Solution: Conduct a detailed analysis of
the  manufacturing  process  and  identify  any  areas  where
improvements could be made to reduce the defect rate.

Hypothesis : The low productivity of a team is due to poor communication
and  lack  of  collaboration.  Solution:  Implement  team-building
activities and communication training to improve collaboration
and communication among team members.

Hypothesis : Customer complaints are due to a lack of quality control in the
production process. Solution: Implement quality control measures
to identify and correct any defects in the production process before
products are shipped to customers.

Hypothesis : High  employee  turnover  is  due  to  a  lack  of  training  and
development  opportunities.  Solution:  Implement  training  and
development programs to help employees develop new skills and
advance their careers within the organization.

Hypothesis : Late delivery of products is due to poor supply chain management.
Solution: Conduct an analysis of the supply chain and identify
areas  where  improvements  could  be  made  to  streamline  the
process and reduce delivery times.

These hypotheses are used to guide the development of solutions and to determine
the effectiveness of those solutions through data analysis and testing in order to
continuously improve the quality of products or services.

8.14 SUMMARY

Benchmarking, if carried out systematically, provides outside views and ideas and
thus  triggers  off  creativity  of  the  group  to  strengthen  its  competitive  capability.
Benchmarking consists of analysis, comparison and synthesis. All these elements are
present in all thetypes of benchmarking except performance benchmarking. Omission
of any of these elements may cause sub-utilization of the potentiality of the concept.
For  example,  use  of  database  for  the  best  practices  does  not  generate  enough
commitments of the personnel concerned as a full-scale study of benchmarking does.
As organizations strive to compete in the highly competitive global economy, it makes
them focus their attention on the customer. QFD links customer requirements of ‘whats’
with the appropriate engineering design characteristics or ‘hows’ so the voice of the

customer is translated into product designs and specifications. Building the House of
Quality is an important step in moving from customer requirements to production
requirements. Proponents of QFD argue that it has several benefits. The study of
organizations implementing QFD demonstrates that it offers product development
teams the opportunity to achieve significant improvements over traditional product
development  practices.  QFD  creates  an  information  intensive  atmosphere  where
communication increases and ideas are freely exchanged. This has a positive impact
on developing product concepts and devising designs that meet customer quality and
performance objectives.

Reliability is concerned with the failure in the field where the product is in use. It
may  be  made  a  part  of  a  requirement  statement,  which  is  later  verified  by
measurement  and  tests.  An  effective  reliability  programme  requires  close
monitoring  of  field  failure.  Like  reliability,  robustness  of  a  design  is  also  an
important element in quality. A product needs to withstand a certain amount of
vagaries when it is in use in the field. Taguchi one of the Japanese Gurus, has
developed  an  off-line  quality  control  methodology,  to  evolve  optimum
specifications through statistical experiments of designs. There should be a proper
encouragement to employees to pay attention to these aspects. Another quality
Guru, Crosby, considers, ‘Zero Defects as the goal for any quality improvement
exercise. He emphasizes management’s consistent campaign and encouragement
to motivate people to work towards zero defects. He has advocated 14 steps as a
part of the implementation of Zero Defects Programme. Incremental improvements
which are normally done on a continuous basis may be an inadequate response to
a situation when an organization needs to improve substantially. An initiative,
called ‘Business Process Reengineering’ is normally undertaken to analyse the
business and develop radically new ways to carry out its certain aspects of it.
Substantial improvement in quality in terms of various dimensions are achieved
through such reengineering initiatives

8.15 KEY WORDS

House of Quality

: A tabular presentation that facilitates planning
of  methods  to  meet  specified  customer
requirements.

Performance Benchmarking: A process of comparison of business results of

Problem Solving Process

several competing organizations.

: A  procedure  commencing  with  selection  of  a
problem till implementation that is followed by
a quality circle in solving each problem.

Process Benchmarking

: A comparison and action planning made for a

Product Benchmarking

Strategic Benchmarking

specified functional process.

: A  process  that  compares  a  product/service,
offered  by  an  organization  with  the  same
marketed by the competitors.

: A process of comparison and learning in respect
of a corporate/business functional strategy.

Tools and Techniques
of TQM

215

Tools and Techniques

Business Process

: An ordered set of activities by which value is

added to inputs.

Reliability Engineering

: A  discipline  to  deal  with  failures  in  order  to

analyse, predict and improve reliability.

8.16  SELF-ASSESSMENT QUESTIONS

1. What is benchmarking? How does it differ from an ad-hoc comparison?

2. What are the different types of benchmarking in relation to objects being

benchmarked?

3. Classify benchmarking based on the nature of organizations against which

benchmarking could be done?

4. What is a process? How does it differ from a function?

5. What are the different kinds of processes?

6. How does benchmarking help an organization?

7. What is QFD? What are the benefits of its application?

8. Explain briefly how you construct a house of quality?

9. What is reliability? Can you define it precisely?

10. Explain the concept of  six sigma.

11. What is the role of hypothesis in TQM?

8.17 FURTHER READINGS

• Charantimath, P. M. (2017). Total Quality Management. Pearson India.

• Cohen, Low and Cohen Louis (1995). Quality Function Deployment : The
Search  for  lndustry  Best  Practices  that  Lead  to  Superior  Performance,
Quality Press, Milwanke, Wisconsin, U.S.A.

• Revelle,  Jack,  Moran  W.  John  and  Cox  Charles.  (1998).  The  QFD
handbook. John Wiley & Sons, U.S.A.  How to make QFD Work for You,
Addison-WeslQ Pub. Co. U.S.A.

• Robson,  Mike.  (1989).    Quality  Circles-A  Practical  Guide,  Ashgate
Publishing Company. Sugimoto, Y. (1972). Japan Quality Control Circles.
Asian Productivity Organization, Tokyo, Japan.

• Rath, S. (2003). Six sigma leadership handbook. New Jersey: John Wiley &

Sons.

•

Sreenivasan, N. S. (2007). Managing Quality: Concepts and Tasks. New Age
International (P) Limited.

• Total Quality Management - I. (2017). CPM, PDPC and Introduction To House
of Quality .NPTEL. https://www.youtube.com/watch?v=BOM5O4lXPLo

216

• Total Quality Management - I. (2017). Six Sigma Overview .NPTEL. https://

www.youtube.com/watch?v=e71AIpPCir4

Tools and Techniques
of TQM

• Winning  Through  Jnnovntiive  Adaptation  Camp,  R.C.  (1989)

Benchmarking:

217

Tools and Techniques

