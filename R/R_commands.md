# Important commands for R

### Author Sudeshna Bora

---
## Basic functionalities

### Installing packages

```
install.packages("<package name>")

```
### Using libraries 

```
library(<library name>)
```
### Assigning to a variable 

```
var_name<-value|expression
```

---
## Data loading

### Loading data 

We load ```iris``` dataset given by R. 

```
data(iris)
```

### Summarising the data 

We get details of the data or any of its column by

```
summary(dataset_name)

or 

summary(dataset_name$column_name)
```

### subset of data

```
subset(dataset_name, column_name == value)
```
---

## Mathematical calculation

### Mean of a column 

```
mean(dataset_name$column_name)

```

### Standard deviation of Column 

```
sd(dataset_name$column_name)
```
---

### Functions for probability distribution

For different types of probability functions, r provide 4 functionalities 

1. p for cumulative density function (p is probability)
2. q for inverse of c.d.f (q stands for quartile)
3. r for random distribution function.
4. d for denstiy function

It is used as a prefix to ```norm```  or ```binorm``` to create the functionality.

```
**Distribution**	**Functions**
**Beta**	pbeta	qbeta	dbeta	rbeta
**Binomial**	pbinom	qbinom	dbinom	rbinom
**Cauchy**	pcauchy	qcauchy	dcauchy	rcauchy
**Chi-Square**	pchisq	qchisq	dchisq	rchisq
**Exponential**	pexp	qexp	dexp	rexp
**F**	pf	qf	df	rf
**Gamma**	pgamma	qgamma	dgamma	rgamma
**Geometric**	pgeom	qgeom	dgeom	rgeom
**Hypergeometric**	phyper	qhyper	dhyper	rhyper
**Logistic**	plogis	qlogis	dlogis	rlogis
**Log** Normal	plnorm	qlnorm	dlnorm	rlnorm
**Negative** Binomial	pnbinom	qnbinom	dnbinom	rnbinom
**Normal**	pnorm	qnorm	dnorm	rnorm
**Poisson**	ppois	qpois	dpois	rpois
**Student** t	pt	qt	dt	rt
**Studentized** Range	ptukey	qtukey	dtukey	rtukey
**Uniform**	punif	qunif	dunif	runif
**Weibull**	pweibull	qweibull	dweibull	rweibull
**Wilcoxon** Rank Sum Statistic	pwilcox	qwilcox	dwilcox	rwilcox
**Wilcoxon** Signed Rank Statistic	psignrank	qsignrank	dsignrank	rsignrank

```

Example of one such is :

```
pnorm(q, mean, standard deviation, lower.tail, log.p)
```
