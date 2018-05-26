This is me re-learning python so I can learn Tensorflow. The `Makefile` lets you run some basic tasks:

## `make`

Installs the dependencies enumerated in `requirements.txt`

## `make eager-intro`

Runs the most basic version of the eager execution paradigm within Tensorflow

## `make tweets.csv`

Given a configuration file, this will download the trending topics and then 1000 tweets from each topic, generating a csv that lists them. This config takes the form of a file named `secrets.json` in the following form:

```json
{
  "CONSUMER_KEY": "XXXX",
  "CONSUMER_SECRET": "XXXX",
  "ACCESS_TOKEN": "XXXX",
  "ACCESS_TOKEN_SECRET": "XXXX"
}
```

## `make rnn`

Given some tweets, use Tensorflow to make an RNN that will simulate more tweets