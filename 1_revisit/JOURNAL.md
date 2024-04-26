# Notes as I go

The first thing I want to do is revisit the original project. The first time I did this, I borrowed heavily from 2 blogs. I did my best to read and understand what they were doing, and out of academic honesty I re-wrote a lot of the code myself. That said, I followed their approach.

I would like to try to not that this time, for a few reasons.
1. One of my goals is to experiment, not just replicate results. There are a number of things (sequence length, filtering & smoothing, lagging variables) that could be experimented with. The previous approach takes at face value how others used them, and is not set up to play around with them and evaluate the impact.

2. Understanding - it's one thing to read and copy, it's another to be intentional about how something is designed and used. I think I will learn more this way.

There is a risk that this turns into rabbit holes and tangential things that I don't really need to know. I'll try to document that as I go, and I expect at some point I am going to get annoyed and move on.

But for now, let's give it a shot!

I have a habit of getting very very ambitious with projects - I get excited thinking about where the final project will go and seeing all the "hinge points" that exist to optimize and add complexity. Need to be very careful! My PM brain needs to prioritize, my engineer brain wants to run wild.

For example - last time I did these projects a jupyter notebooks. I had a separate notebook for each data set. I could:
1. Try to set it up to run everything in a single notebook
2. Get even more creative and build this as an actual application

Idea 2 seems like fun but perhaps way too ambitious. What I could do instead is try to build out functions i'll need in a util folder and import that into a notebook. The benefit of the notebook is that it makes it easy to add in visualization and re-run things.

## What do I need to do?

At a high level, as I understand things:

1. I need to import the data sets I am going to use
2. Choose which sensors I will be using
3. Create a set of matrices a "run" of sensor readings paired with the known remaining useful life
4. Feed this data to a model to test
5. Evaluate the outputs

3 has a lot of things I can do with it
1. I can vary the sequence lenght - this could be thought of as varying the context window. My hypothesis is that longer is better up to some point. Too long is bad because a) less training data and b) more noise
2. To the noise part - I can try to "clip" our steady state operations. Presumably there is a long time where nothing is really happening and then a period where the engine deteriorates and we get a lot of information.
3. Filtering - the other project did something called exponential smoothing. What is that? There's lots of signal processing techniques to filter out noise. Maybe it's worth doing something like that?
4. Lagging data - Why did I do this last time? I could imagine that it's to capture inter-temporal relationships, but I kinda assumed that's what the model is supposed to do on it's own. Is this just adding bias?

I think there's also a lot I can do with the model itself. I recall being able to vary the architecture (number of layers, adding other network types and layers and stuff). I also could very the epochs and things like that.

Another interesting thing is that my current laptop is waaaay better than what I used last time. I hope that means it's a lot faster!!

## Approach

I'll break the application into 3 parts

1. Import data and all tools needed
2. Based on the parameters chosen, create the training data sequences
3. Based on the parameters chosen, train the model, evaluate it, and output data for analysis
4. Given results, create graphs <- maybe? This might be more worth exploring side-by side

I am hopeful that this will all be extensible to future models - transformers and MAMBA or whatever else would just be a new verion of 3 and I don't have to change much about 1, 2, or 4. 

In any case, I can write an application that intakes some set of test paramters (what to vary, how to vary it, etc...), creates all the sequences, does all the training and testing, and outputs the results

The risks I foresee are this is gonna be a lot of work (fun!), it will go too slow, and it will crash and be hard to audit

Well - one way to find out!!

## 3/26/2024

I understand the input format!! This was probably the most confusing thing last time - what do I need to do to go from "I have this data" to "use it to predict".

This blog was very helpful in visualizing the problem-> https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/

There are three inputs:
1. Samples - for my project, this would be each "bactch" of sequences
2. Time Steps - which point in the seuquence we are at
3. Features - each sensor reading at a given step in the sequence

This makes so much sense haha

So - this is very clarifying. What I need to do:

1. Choose the features to include
2. Slice them into T x F arrays
3. Package the arrays together into a S x T x F array

An interesting question is adding more features. The beuty of ML is supposed to be that it magically figures this out for you - but this blog post shows that in some cases lagged data improves performance. In theory, RNNs should be able to capture any inter-temporal relationships. This would be a very good future experiment.

Another idea - could you package samples of varying sequence lengths and then pad them? Why? Perhaps there is additional information to be gained by looking at different sequence lengths? If we find that varying sequence length has any predictive power, then perhaps we can get additional information by considering the same sample but focusing on different lenghts. The fact that lagging helps at all seems to suggest this might too. Could also lead to over-fitting.

I'm thinking for this first version, I should keep things very simple and just build out the sequencing code. In the future, I can pre-process.

Also just learned what a generator function is - chat GPT is really better than google for learning. I would have learned so so so much faster with chat GPT explaining things for me. I think it raises the bar in what you can be expected to accomplish. 
