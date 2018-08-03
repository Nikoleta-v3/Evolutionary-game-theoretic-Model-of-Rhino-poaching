# Reviewer 1

>> Ln 58 pg 5, repeated "of"

**Action:** Remove second "of"

>> Ln 20 – 40, pg 6, the variables talk about "proportion of horn gained" but I think
a more general way to think of the variable is "proportion of value gained from the horn".
For example, de-horning clearly leads to proportion of horn, but for other management
interventions such as dye it may be a proportion of devaluing rather than quantity.
Think it would be useful to say something like this model holds for any management action
that proportionally devalues or removes a quantity of horn from the market, we will use
the word "horn gained" because we are thinking about "dehorning" but the model is more
general, or something to that effect.

**Action:** Yes, reword to "proportion of value gained from the horn" and add a
sequence of how our model can be applied to other devaluation methods. We
suggest also ensuring that the language throughout is in terms of devalued and
not dehorned rhinos.

>> Eqn 5, There are many mathematically valid choices for how to write this equation,
including yours, but I think this way of expressing it is less clear than some alternatives.
I think it would be clearer to write this equation in one of the following ways,
>> x(1-r) + (1-x)(1- r + r sigma_r) or
>> 1 – r + r sigma_r (1-x)
>> to me your choice of expression obfuscates the meaning and creates an awkward nested
parenthesis. Of the two expressions above, the first one starts from the point of view
of the proportion of poachers, the alternative equation starts from the point of view
of the rhino (i.e. whole horns are harvested from both types (1-r) and r sigma_r (1-x)
is the additional value harvested by the indiscriminate poachers. The second is the
simplest expression in my opinion, but I can see reasons for why you might prefer
the former one.

**Action:** Yes, re-write, potentially include both forms?
Similarly for equation (8).

>> Ln 55-56 pg 6, can you avoid introducing the variable capital x. Simply say as you
basically do in the following line, that x uniquely determines the proportion of
both types and therefore describes the state of the population of poachers. The added
variable is unnecessary unless you are going to use it heavily later.

**Action:** Remove \(\chi\) and move the sentence about removing it to earlier.

>> Eqn 6 is confusing as to how it should exactly be thought of and how it relates to
supply and demand relationships. It is not clear how fig.2 shows how "fig 2 verifies
that the gain curve corresponds to a demand curve". How exactly does it do this?

**Action:** Talk about \alpha and how it will allow us to capture the behaviour
of supply demand, but need to explain the supply demand relationship. We can do
this by adding more explanation surrounding the figure. "We see that when the
supply of rhinos is high, ie a low level of r, the value is low and vice versa".
Also, include a very clear sentence saying that \(H, \alpha\) are scaling
parameters that ensure the needed gradient.

>> Eqn 9, this is a bit strange to me, why is this an exponent? Consider that each rhino
dehorned caused a unit of money that could go to security, then dollars to security is
directly proportional to (1 – r) so why not a constant multiple? Presumably if beta < 1
this could denote a diminishing return on police efficacy

>> Eqn 8, I do not understand this equation. What is this the cost of? Searching for rhinos?
Presumably this could be measured in the amount of time it took to find a rhino comparatively
if you were passing on rhinos that have been devalued. If we were assuming poachers
encountered rhinos randomly via laws of mass action for every time unit it took for
indiscriminate poachers to find a rhino it would take 1/(1-r) units of time for an
indiscriminate poacher to find a rhino that hasn't been devalued. Is this how equation
8 is being calculated? If so I do not follow the derivation. I’m also concerned with
double counting. Your benefit function includes the added benefit from poaching rhinos
indiscriminately by getting more rhinos. Please walk the reader through this equation.
Is it search cost? Is this the same cost for an individual of both strategies? I’m not
really sure what you are assuming here.

>> Eqn 5 – 11, Handling time of killing and processing a rhinos and the increased risk of
being caught due to killing more rhinos (dehorned rhinos) do not appear to be factored
into the model. As a result I question whether the main result is an artefact of this
model set-up. I’m not sure I follow how an discriminant poacher gets any benefit from
their actions in this model (with the exception of H). I don't think supply and demand
is the main reason managers argue for this strategy, so the effect of H is less important
to explore than handling time and risk to poachers, in my opinion. From a game theoretic
sense, unless I am missing something, it is obvious that increases in H with r wouldn't
affect the stable strategies because all individuals are affected by the price of
the value of horn equally. So only through risk of exposure and added costs through
handling time of killing less valuable rhinos can one argue for dehorning, which this
paper doesn't explore.

>> Eqn 11 confuses me as I thought time would be the unit of cost of searching for rhinos,
as can be seen from my comment above I thought something like these equations would be
the costs. Basically I was expecting equation 11 to be the costs. It seems like we have
similar thoughts. Psi actually seems to just be proportional to the number of rhinos
being poached, but you call it the cost, which is confusing to me. Am I missing
something here?

**Action:**

For all of the above: we are going to express the cost of poachers in "simpler"
terms:

- Likelihood of being caught by security: \((1 - r) ^ \beta\) 
- Time spent in the park

Time spent in the park will be calculated differently for each type of poacher
under the assumption that all poacher aim to "get" "1" amount of horn before
leaving. (The comment of having a linear multiplicative constant will take care
of itself as it will just be what is currently F).

TODO: Do the formulation and rewrite
TODO: Code up the formulation and code a simulation of it.
TODO: Redo all theoretic results

>> Similar to the capital X comment this sentence is also confusing. Just introduce s.

**Action:** The reviewer here talk about sigma, remove sigma

>> When introducing H I think you need a reference for its choice. Below are some modelling
papers where supply and demand affecting poaching

- [Economics of Antipoaching Enforcement and the Ivory Trade Ban](https://www.jstor.org/stable/1244594?seq=1#page_scan_tab_contents) 
- [Protecting the African elephant: A dynamic bioeconomic model of ivory trade](http://www.unece.lsu.edu/responsible_trade/documents/2008/rt08_33.pdf)

**Action:**

>> There are many papers modelling poaching in the rhino trade system. You might want
to consider going through them a bit more systematically and describing how your work
sits within the broader rhino horn modelling literature (possibly in the discussion).
Here are some examples (but there are many more) to seed your search

- [Debunking the myth that a legal trade will solve the rhino horn crisis:
A system dynamics model for market demand](http://www.saeon.ac.za/enewsletter/archives/2015/october2015/images/0300.pdf)
- [Identification of policies for a sustainable legal trade in rhinoceros horn based on
population projection and socioeconomic models.](https://www.ncbi.nlm.nih.gov/pubmed/25331485)
- [Trading on extinction: An open-access deterrence model for the South African abalone
fishery](http://www.scielo.org.za/scielo.php?script=sci_arttext&pid=S0038-23532016000200019)
- [How many to dehorn? A model for decision-making by rhino managers](https://www.cambridge.org/core/journals/animal-conservation-forum/article/how-many-to-dehorn-a-model-for-decisionmaking-by-rhino-managers/63CBEF4F8929487E3420AD41BADF601B)

**Action:**

>> It would be good to cite the anthropogenic Allee effect in either line 42 of the
intro or in the discussion as this is one of the main hypothesised drivers in the
mathematical modelling literature on what causes rhino horn to be so valuable.
The theory is mathematically described in

- [High prices for rare species can drive large populations extinct: the anthropogenic
Allee effect revisited.](https://www.ncbi.nlm.nih.gov/pubmed/28669883)

>> and first biologically hypothesized here

- [Rarity Value and Species Extinction: The Anthropogenic Allee Effect](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0040415)

**Action:**

>> Ln 42 pg 3 of intro, it doesn't make sense to talk about quadrants without a figure
to refer to with quadrants in it, or to say the poachers win (win at what).

**Action:** Reword this. It was left from removing Fig 1

>> Ln 20 – 43 pg 3. The issue of opportunistic exploitation is highly relevant to the
game you present. In fact I think it may be the logic behind a lot of what's driving your
results. It's not exactly the same because the authors think of opportunistic exploitation
as a multi-species problem, but it is very similar because you could think of dehorned
and horned rhino as two species. The basic idea is that while hunting for one type
you will kill the other if it's there and easy to kill without much added cost.
Ln 20 -43 seems like a natural place to talk about this, but it could be talked
about later in the discussion

- [Opportunistic exploitation: an overlooked pathway to extinction](https://www.sciencedirect.com/science/article/pii/S0169534713000712)

**Action:**

>> Ln 46, pg 3, space after period

**Action:** Remove space

>> Eqn 1 these are also often called replicator equations in the evolutionary dynamics literature

- [Evolutionary Dynamics](http://www.hup.harvard.edu/catalog.php?isbn=9780674023383)

**Action:**

>> Lines 36 – 38, not really. This is only true if parks are very small and there is
relatively small amounts of travel time to get between the parks. Perhaps use the
hedging phrase "may also provide insights at the macroeconomic level." I also think a
discussion of travel time might be warranted here and what assumptions must be made
for this model to hold in the macroeconomic case.

**Action:**

Add required discussion.

# Reviewer 2

>> I think the most problematic assumption is that rhino population dynamics is assumed
to be stable through time. Obviously, this won't be the case and that could change
everything because the increasing rarity of rhino could increase the price of horn,
devalued or not, and therefore the relationship between costs and benefits that would
be challenging to predict. I think addressing this question could definitely increase
dramatically the novelty of this study, which will be beneficial from an ecological and
a modelling point of views.

**Action:** Address this by adding a line about (1 -r) as discussed with Vince

>> The authors have also identified some situations were selective strategy could be
more beneficial than indiscriminate. I think it could be interesting to look at the
literature in which kind of situations we really are, and if these conditions found
theoretically can be really encountered on the field.

**Action:** Investigate

>> Regarding the length of the paper, I am not 100% sure that the analysis for situations
where everyone has selective or indiscriminate strategy really brings something.
This highlight that this study is maybe not deep enough, because classically, these analyses
would be moved in supplementary materials. I understand the point of showing the
difference with mixed strategies, which won't be stable, but I still think these
analyses on pure strategies are not very insightful.

**Action:** Possible remove some theorems or just put some together

>> Finally, from a presentation point of view, I think that figure 1 is not needed

**Action:** Remove figure add more the discussion of ess

>> Figure 2 and 3 could be merged.

**Action:** possible merge

>> Legends and axes names need to be improved to make the figures readable without going back to the text.

**Action:** Make bigger.

>> I think that a summary figure of the selected strategies (without discentive) could be also an interesting addition.

**Action:** Ask Tamsin if she understands what is wanted here.
