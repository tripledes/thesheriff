Conclusions
===========

The next paragraphs will contain a small summary of the lessons
learned in the project, comments about the development, acquired
knowledge and a evaluation of the product.

The first consideration commented between those who form
*The Sheriff Team* is that we didn't expect to deliver something
that was going to work in this short period of time.
We were frightened of the fact that we had to deliver a project
from scratch in less than two months.
Now that tests are passing and we have a final code organised
and clean, we are very proud of the achieved result.

The second consideration is that *The Sheriff Team* is formed
by people with very different work experience in the programming world.
Taking this into account, we consider that all of us, every one
in his own level, has learnt a lot and has had the opportunity to
apply the concepts learnt in class. Mostly in design concepts, but also
in how to build a correct infrastructure, the level of knowledge of every
one has grown a lot.

Given the different background of the team members, selecting technologies
was a bit of a challenge, specially the programming language. The team
settled for Python, for its lower learning curve, but it did bring its own
set of tradeoffs. For instance, Python is not strongly typed, though since
some versions it allows to define the types of the data being used, it's
still not strongly enforced.

After dealing with Python tradeoffs, we had to pick libraries, at this point
the team realized that most of the available frameworks forced some concepts
that the architecture selected would just be impossible. So the team settled
for using *Flask* and *SQLAlchemy Core* (**no ORM**), both brought some ease
to the development without getting in the way of the architecture. Finally,
a dependency injection package was required because without using the whole
frameworks, that part was left for the team to implement. Luckily, another
small third-party library was found *inject*, which provided the required
features.

That being said about Python and its frameworks, the team still found Python
easy to use, which helped into prototyping a 
:abbr:`MVP (Minimum Viable Product)` quickly and without much overhead.

Last but not least some functionality is still pending to work properly and
due lack of time we prefer to focus on documentation and sumarize decisions
taken during the development. So you could find a couple of FIXME within the
code and even non-closed issues in github in order to not lose the track of those
future enhancements.
