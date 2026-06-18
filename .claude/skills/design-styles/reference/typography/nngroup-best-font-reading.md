# Nngroup Best Font Reading

10

# Best Font for Online Reading: No Single Answer

 Jakob Nielsen

 Jakob Nielsen

 April 24, 2022

 2022-04-24

 Share

 -

 Email article

 -

 Share on LinkedIn

 -

 Share on Twitter

 Summary:
 Among high-legibility fonts, a study found 35% difference in reading speeds between the best and the worst. People read 11% slower for every 20 years they age.

 A large new study of the best fonts for online reading is ultimately disappointing, because it doesn’t answer the most burning question: what font should you use for your website? But it still provides many intriguing findings, including the striking conclusion that there is no single answer to this question.

##
 In This Article:

-
 The Research Study

-
 Fonts Matter

-
 Main Finding: No Best Font for All Users

-
 Can’t Ask Users

-
 Age Differences

-
 A Possible Solution for Font Optimization

-
 Conclusion

## The Research Study

Shaun Wallace from Adobe and colleagues conducted a reading-speed study with 352 participants. The participants were asked to read several short passages of text; each passage had 300–500 words (by comparison, this article contains 2,623 words and the average web page contains 593 words). The test stimuli were at an approximate 8th grade reading level, which matches our recommendation for web content targeted at a broad consumer audience . (This article is written at a 12th grade reading level, but it targets professionals , not the general public.)

The texts were shown in 16 different fonts, with appropriate experimental controls for things like order effects.

Fonts included classic typefaces (Times, Helvetica, Garamond), typefaces designed for computer use (Calibri, Arial), and typefaces specifically designed for legibility (Noto Sans, Montserrat); no “wild” fonts (think ) were included. However, each user only read texts in 5 of these fonts during the main reading-effectiveness test.

While navigating the Internet, users mostly scan pages for useful information , as opposed to reading all the text word-for-word. Thus, in real life, users only read 28% of the words on a webpage, or about 166 words. In contrast, study participants did read the entire texts in a linear fashion. (Complete reading was encouraged by asking users a few comprehension questions after they had finished reading each passage.)

This difference in reading behavior between web users and study participants does raise the question whether findings would be different under more realistic web-usage conditions. Even so, I still think the findings about the relationship between fonts and reading speed are of interest.

The authors note that there are 3 types of reading, of which they only studied one:

- Glanceable reading of a few words, as found in notifications and on tiny screens like smartwatches

- “Interlude” reading: reading of short passages of prose like the ones used in the study and found on most websites

- Long-form reading, for example reading of a book

The three main metrics collected were:

- Subjective user preference: which font did each person like the best?

- Reading speed in words per minute (WPM)

- Comprehension score: percent of questions answered correctly after the user finished reading a passage

However, this last metric was not very interesting, as the score was very close to 90% in all conditions. High comprehension indicates that (a) the content was easy relative to the users’ reading skills, and (b) people read the texts carefully. The first of these findings is not always true for web content, and the second is rarely true for web users.

## Fonts Matter

On average, any given participant read 35% faster in his or her fastest font (314 WPM) compared to that same person’s slowest font (232 WPM, on average). This is a huge difference, considering that each user was only measured on 5 fonts. If reading speeds had been measured for all 16 fonts for each user, the difference between the fastest and slowest font would have been likely even bigger. And it would have been bigger again in a hypothetical (but impossible) experiment that measured people reading texts in all available fonts with sufficient legibility to be considered for practical business design. (Impossible, because there are probably thousands of good fonts, not even considering the even larger number of bad fonts which we sadly do see employed on websites from time to time.)

 These 16 typefaces were measured in the study. For each font we show users' average reading speed in words per minute (WPM).

## Main Finding: No Best Font for All Users

With this big difference in reading speeds within users, you would expect that the study would have identified a font with the highest overall score. Well, it did: Garamond had the highest average reading speed at 312 WPM; it was 6% better than #2 (Oswald, at 295 WPM) and 23% better than the worst font of the 16 tested (Open Sans, at 254 WPM).

But Garamond was only best on average . It wasn’t best for all users . There were substantial individual differences.

Many users were faster readers with another font than Garamond, which means that they would be penalized by a design that used Garamond. The authors also computed a speed-rank score that shows how often a font was the fastest of those 5 fonts that a given user saw. Garamond only achieved a speed rank of 48%, which means that (slightly) more than half of the time another font would be better for a specific user. (And an even bigger percentage would likely have been better off with a different font than Garamond if all 16 fonts had been available as alternatives.)

 The highest speed rank was achieved by Franklin Gothic, at 59%. Note that this still means that 41% of users would be better served by a different font out of the 5 they used. Interestingly, Franklin Gothic only scored an average reading speed of 271 WPM, which is much lower than Garamond’s reading speed of 312 WPM. In other words, Franklin Gothic is better for more people than Garamond, but the mean speed is higher for Garamond. How to explain this discrepancy? It's possible that Franklin Gothic is a good font for poor readers, whereas Garamond is good for strong readers. If true, the strongest readers can really speed ahead with Garamond and drive up its overall mean. (Remember that the mean of 2 and 4 is 3, whereas the mean of 2 and 10 is 6. Thus, if the high end can be increased in a dataset, then the mean will increase even if the low end stays the same.)

Whatever the true cause, the distinction between Franklin Gothic and Garamond is simply more proof of the overall finding that different fonts are best for different people, with reading skills being a possible differentiator impacting font choice.

## Can’t Ask Users

If different fonts are best for different people, you might imagine that the solution to the fonts problem would be a preference setting to allow each user to select the font that’s best for them.

This solution will not work, for two reasons. First, previous research on user-interface customization has found that most users don’t use preference settings, but simply make do with the default .

Second, and worse, users don’t know what’s best for them , so they can’t choose the best font, even if they were given the option to customize their fonts. In this study, participants read 14% faster in their fastest font (314 WPM, on average) compared to their most preferred font (275 WPM, on average). Again, each individual user in this study was only measured on 5 fonts, whereas most systems have many more. For example, the word processor I am using to write this article has more than 200 fonts installed (of which, admittedly, several are script fonts that no sane person would pick for reading). More fonts equal more chance of picking wrong and a larger difference in reading speed between the optimal font and the user’s choice.

## Age Differences

 Users’ age had a strong impact on their reading speed, which dropped by 1.5 WPM for each year of age. It’s important to note that this is not a matter of young users vs. senior citizens. The average age of the study participants was 33 years, with a spread from 18 to 71 years, but a small bias in favor of younger users.

Reading speed drops during middle age. A 20-year age difference (for example, from 20 to 40, or from 30 to 50 years old) will, on average, correspond to reading 30 WPM slower , meaning that a 50-year old user will need about 11% more time than a 30-year old user to read the same text. (Computed relative to the overall average reading speed in the study, which was 276 WPM.)

By comparison, in an earlier study, we found that users between the ages of 25 and 60 declined in performance by 0.8% per year , in terms of the time needed to perform tasks while using websites. A performance drop of 0.8% per year corresponds to users spending 16% more time to perform tasks on websites if they are 20 years older .

How to explain that the performance decline caused by 20 years of aging was 16% in the website-usage study but only 11% in the online-reading study? One explanation is simply the passage of time: there were about 14 years between the two studies, with the bigger difference measured in 2007 and the smaller difference measured in 2021. During these 14 years, older people have become more tech-savvy and possibly also have better health due to advances in medical care. Today’s 40-year-olds probably exercise more and pop more prescription pills, which may make their brains decay a little slower than was the case for the previous generation.

Another explanation (which I personally believe to be more plausible) is that two different things were measured. Yes, performing tasks on websites involves reading, but it also requires many more advanced skills, such as navigation, search, and the ability to judge and make decisions based what’s being read. It is likely that the degradation of the human brain during middle age is more damaging for people’s ability to do complicated things than for the performance of relatively simple functions such as reading.

A second interesting age-related finding from the new study is that different fonts performed differently for young and old readers . The authors set their dividing line between young and old at 35 years, which is a lower number than I usually employ, but possibly quite realistic given the age-related performance deterioration they measured.

3 fonts were actually better for older users than for younger users: Garamond, Montserrat, and Poynter Gothic. The remaining 13 fonts were better for younger users than for older users, which is to be expected, given that younger users generally performed better in the study.

The takeaway is that, if your designers are younger than 35 years but many of your users are older than 35, then you can’t expect that the fonts that are the best for the designers will also be best for the users.

Also, the differences in reading speed between the different fonts weren’t very big for the young users. Sure, some fonts were better, but they weren’t much better. On the other hand, there were dramatic differences between the fastest font for older users (Garamond) and their slowest font (Open Sans). In other words , picking the wrong font penalizes older users more than young ones . The same takeaway applies: if the designers are young, they may not experience much reading-speed differences between different fonts, leading them to make design decisions based on mainly aesthetic criteria and assuming legibility to be less important. But those fonts that seem pretty much equally legible to young people can have vastly different legibility for older people. (And remember that “old” was defined as 35 years or above in this study.)

A final point about age differences in reading: the study didn’t include many true seniors, topping out at 71 years for its oldest participant. In our first user research with senior citizens in 2002, we defined “seniors” as users aged 65 and above. But in our latest research with seniors (2019), we discovered that people in their late 60s use computers pretty much the same as people in their 50s. Thus, they don’t need special usability guidelines, and we don’t consider them as seniors anymore. Now, our definition of seniors is users aged 70 years and above. This group does need special usability guidelines, and even though we haven’t specifically measured their reading speed, it is likely that the decline in reading speed will progress at a faster pace in these higher age groups. Since the new research found differences in the best fonts for people younger and older than 35 years, it’s very likely that further research might find even more differences in the fonts that would be best for users aged 70 and above.

## A Possible Solution for Font Optimization

Purely as speculation, I tried to invent a system to give individual users the best font to maximize their reading speed.

It should be possible to use personalization to present individual users with text in the font that’s best for them. A browser or e-reader would initially present text in a randomly chosen font. After enough time has passed to generate a reliable estimate of the user’s reading speed with this font, the system would change to another font and use it until there’s a reliable estimate of that font’s reading speed. Repeat this process many times, and eventually the specific user’s reading speed will have been measured for several fonts. Whatever one wins can then be used going forward.

Since we know that there are age-related changes in font performance, we should repeat the font-optimization process every few years, to identify a new font that would be better for the now-older user.

It would be unpopular to present text in ever changing fonts during the long calibration procedure, and then spring a new font on the user a few years later. (Certainly, this is a violation of usability heuristic #4 which calls for consistency .) I am not seriously suggesting this solution, and it would probably be better as an April Fools’ Day story . But since I have demonstrated that it’s possible to automate the selection of an individually optimized font, maybe there will one day be a practical system for doing so.

## Conclusion

The new study is ultimately disappointing because it doesn’t provide us with actionable design guidelines. But it offers substantial new insights into online reading that will make us think harder about how to design text-heavy web pages:

- Even among fonts with good legibility, reading speeds differ substantially, so it really matters to get the font right.

- Unfortunately, no single font is best for all users.

- We can’t ask users to choose their own font, because people won’t pick the font that’s best for them.

- Reading speed declines substantially with age, even among middle-aged users. We’ve always recommended to cut the words for digital content , but now we should recommend cutting 11% more words if large parts of your audience are 50 years or older.

- There are age-related differences in what fonts are best, with people younger than 35 (most designers) being different than people older than 35 (most users). Oh, well, you are not the user , as we always say.

Clearly, as scientists like to say, more research is needed. Given the findings in the new study, the answer will not be simple, but we can still hold out a little hope that it might prove possible to derive a formula that could predict the best font for a given user, given multiple criteria (not just one criterion, sadly). We also need an experimental protocol that more closely mirrors the typical scanning behavior of web users.

Finally, even though this study didn’t include any bad fonts, there are some low-legibility ones out there. Do stay away from those, because they can reduce reading speeds by much more than the numbers discussed here. And even with good fonts, avoid tiny text and low contrast , both of which do much damage.

### Reference

Shaun Wallace, Zoya Bylinskii, Jonathan Dobres, Bernard Kerr, Sam Berlow, Rick Treitman, Nirmal Kumawat, Kathleen Arpin, Dave B. Miller, Jeff Huang, and Ben D. Sawyer (2022): Towards Individuated Reading Experiences: Different Fonts Increase Reading Speed for Different Individuals . ACM Transactions on Computer–Human Interaction , Volume 29, Issue 4, Article No. 38.

## Related Courses

 -

#### Visual Design Fundamentals

 Create user interfaces using essential principles, techniques, and methods of visual design

 Interaction

 typography,readability,Writing for the Web,age effects,older users

## Related Topics

 -
 Writing for the Web

 Writing for the Web

## Learn More:

 -

 The 3 Sizes of UX Copy

 Taylor Dykes

 &centerdot;
 5 min

 -

 Demystifying Clickbait: You’ll NEVER Believe What I Learned

 Taylor Dykes

 &centerdot;
 7 min

 -

 3 Tips to Make AI a Better Editor

 Taylor Dykes

 &centerdot;
 7 min

## Related Articles:

 -

 Typography Terms: Glossary

 Sarah Gibbons and Therese Fessenden

 &centerdot;
 7 min

 -

 Privacy Policies and Terms of Use: 5 Common Mistakes

 Therese Fessenden

 &centerdot;
 9 min

 -

 The Layer-Cake Pattern of Scanning Content on the Web

 Kara Pernice

 &centerdot;
 8 min

 -

 Typography for Glanceable Reading: Bigger Is Better

 Page Laubheimer

 &centerdot;
 7 min

 -

 Serif vs. Sans-Serif Fonts for HD Screens

 Jakob Nielsen

 &centerdot;
 5 min

 -

 Inclusive Design

 Alita Kendrick

 &centerdot;
 6 min