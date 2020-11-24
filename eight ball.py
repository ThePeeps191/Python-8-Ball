def _8ball():
  while True:
    import random
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    inp = input("Enter Your Question:\n")
    out = random.choice(responses)
    print(f"Your Question: {inp}  The 8 Ball's Answer: {out}")
    yes_or_no = input("Would You Like To Try Again?(y/n)\n")
    if yes_or_no == "n":
      break

_8ball()
