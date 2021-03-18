![](https://img.shields.io/badge/Chess-red)
![](https://img.shields.io/badge/Python-blue)
![](https://img.shields.io/badge/PGN-yellow)

# pgn2fixture

A module that translates PGN files into Django fixtures

## How it works

### Install

`pip install pgn2fixture`

### Usage


If we have the following PGN game:

```
[Event "USSR Championship"]
[Site "Moscow URS"]
[Date "1955.03.12"]
[EventDate "1955.??.??"]
[Round "18"]
[Result "1-0"]
[White "Boris Spassky"]
[Black "Viktor Korchnoi"]
[ECO "D87"]
[WhiteElo "?"]
[BlackElo "?"]
[PlyCount "81"]

1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. cxd5 Nxd5 5. e4 Nxc3 6. bxc3 Bg7 7. Bc4 O-O 8. Ne2 c5 9. O-O Nc6 10. Be3 Bg4 11. f3 Na5 12. Bxf7+ Rxf7 13. fxg4 Rxf1+ 14. Kxf1 cxd4 15. cxd4 Qd7 16. h3 Qe6 17. Qd3 Qc4 18. Qd2 Qa6 19. Qc2 Nc4 20. Qb3 Kh8 21. Kg1 Nd2 22. Bxd2 Qxe2 23. Be3 Rf8 24. e5 b5 25. Rc1 a5 26. Bg5 h6 27. Bxe7 a4 28. Qd1 Qe3+ 29. Kh1 Rf2 30. Qg1 Qf4 31. a3 Kh7 32. Bc5 h5 33. gxh5 Bh6 34. hxg6+ Kg7 35. Re1 Qg3 36. Bb4 Be3 37. Qh2 Qg5 38. e6 Bf4 39. Qg1 Qh4 40. e7 Rf3 41. Qh2 1-0
```

We can load it into pgn2fixture as follows:

```
from pgn2fixture import pgn2fixture

pgn = raw_pgn
game = pgn2fixture.Game(pgn)
```

From then on, the `game` object will provide access to the PGN seven roster tag as follows:

```
game.white # => Boris Spassky
game.black # => Viktor Korchnoi
```

All standard PGN roster tags are accessible via properties. All non-standard tags included in the raw PGN will be accesible via the `game.tags` variable, which contains all tags from the PGN as Python dictionary such as the following:

```
    {'event': 'USSR Championship', 
     'site': 'Moscow URS', 
     'date': '1955.03.12', 
     'eventdate': '1955.??.??', 
     'round': '18', 
     'result': '1-0', 
     'white': 
     'Boris Spassky', 
     'black': 'Viktor Korchnoi', 
     'eco': 'D87', 
     'whiteelo': '?', 
     'blackelo': '?', 
     'plycount': '81', 
     'moves': '1. '1. d4 Nf6 2. c4 g6 etc'}
```

In order to convert the `game` object into a Django fixture dictionary, just call the method `to_fixture()` as follows:

```
game.to_fixture(model: str)
```

where the argument `model` is a string with the name of the Django model. 
As for the PK for the database, you will need to implement a way to create them as you need them.

## Author

👤 **Josias Alvarado**

- GitHub: [@pointerish](https://github.com/pointerish)
- Twitter: [@pointerish](https://twitter.com/pointerish)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/josias-alvarado/)
- [Blog](https://josias-alvarado.me)

## Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/pointerish/pgn2fixture/issues).


## License

This project is [MIT](LICENSE) licensed.