from bot import Bot

WELCOME_MESSAGE= " ╭╮╭╮╭╮╱╱╭╮\n \
┃┃┃┃┃┃╱╱┃┃\n \
┃┃┃┃┃┣━━┫┃╭━━┳━━┳╮╭┳━━╮\n \
┃╰╯╰╯┃┃━┫┃┃╭━┫╭╮┃╰╯┃┃━┫\n \
╰╮╭╮╭┫┃━┫╰┫╰━┫╰╯┃┃┃┃┃━┫\n \
╱╰╯╰╯╰━━┻━┻━━┻━━┻┻┻┻━━╯\n \
╭━━━━╮╱╱╱╭━━━━╮╱╱╱╱╱╭━━━━╮\n \
┃╭╮╭╮┃╱╱╱┃╭╮╭╮┃╱╱╱╱╱┃╭╮╭╮┃\n \
╰╯┃┃┣╋━━╮╰╯┃┃┣┻━┳━━╮╰╯┃┃┣┻━┳━━╮\n \
╱╱┃┃┣┫╭━╯╱╱┃┃┃╭╮┃╭━╯╱╱┃┃┃╭╮┃┃━┫\n \
╱╱┃┃┃┃╰━╮╱╱┃┃┃╭╮┃╰━╮╱╱┃┃┃╰╯┃┃━┫\n \
╱╱╰╯╰┻━━╯╱╱╰╯╰╯╰┻━━╯╱╱╰╯╰━━┻━━╯"
DRAW_TXT = " ╭━━┳╮╱╱╱╱╱╱╱╱╱╭━━━╮\n \
╰┫┣╯╰┳╮╱╱╱╱╱╱╱╰╮╭╮┃\n \
╱┃┣╮╭┫┣━━╮╭━━╮╱┃┃┃┣━┳━━┳╮╭╮╭╮\n \
╱┃┃┃┃╰┫━━┫┃╭╮┃╱┃┃┃┃╭┫╭╮┃╰╯╰╯┃\n \
╭┫┣┫╰╮┣━━┃┃╭╮┃╭╯╰╯┃┃┃╭╮┣╮╭╮╭╯\n \
╰━━┻━╯╰━━╯╰╯╰╯╰━━━┻╯╰╯╰╯╰╯╰╯ \n"
X_TXT = " ╭━╮╭━╮ ╭╮╭╮╭┳━━┳━╮╱╭╮\n \
╰╮╰╯╭╯ ┃┃┃┃┃┣┫┣┫┃╰╮┃┃\n \
╱╰╮╭╯  ┃┃┃┃┃┃┃┃┃╭╮╰╯┃\n \
╱╭╯╰╮  ┃╰╯╰╯┃┃┃┃┃╰╮┃┃\n \
╭╯╭╮╰╮ ╰╮╭╮╭╋┫┣┫┃╱┃┃┃\n \
╰━╯╰━╯ ╱╰╯╰╯╰━━┻╯╱╰━╯\n"
O_TXT = " ╭━━━╮ ╭╮╭╮╭┳━━┳━╮╱╭╮\n \
┃╭━╮┃ ┃┃┃┃┃┣┫┣┫┃╰╮┃┃\n \
┃┃╱┃┃ ┃┃┃┃┃┃┃┃┃╭╮╰╯┃\n \
┃┃╱┃┃ ┃╰╯╰╯┃┃┃┃┃╰╮┃┃\n \
┃╰━╯┃ ╰╮╭╮╭╋┫┣┫┃╱┃┃┃\n \
╰━━━╯ ╱╰╯╰╯╰━━┻╯╱╰━╯\n"
class Tic_Tac_Toe():

    def __init__(self) -> None:
        self.board = " 1 | 2 | 3 \n------------\n 4 | 5 | 6 \n------------\n 7 | 8 | 9 \n"
        print(WELCOME_MESSAGE)
        print(self.board)
        self.x_score = []
        self.o_score = []
        self.bf = []
        self.x = "human"
        self.o = "human"

    def ending(self, winner):
        if winner == "X":
            print(X_TXT)
        else:
            print(O_TXT)

    def check_win(self, score):
        winning_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                        [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for combo in winning_list:
            if all(num in score for num in combo):
                return True
        return False

    def check_draw(self):
        return len(self.bf) == 9

    def play_turn(self, player):
        if self.x == "Bot" and player == "X":
            bot = Bot()
            block = bot.make_move(blocks_played=self.bf,
                                  ops_moves=self.o_score,
                                  own_moves=self.x_score)
        elif self.o == "Bot" and player == "O":
            bot = Bot()
            block = bot.make_move(blocks_played=self.bf,
                                  ops_moves=self.x_score,
                                  own_moves=self.o_score)
        else:
            while True:
                try:
                    block = input(
                        f"It's {player}'s turn. Choose your block:\n{player}의 차례입니다. 블록을 선택하세요: "
                    )
                    if int(block) not in range(1, 10) or int(block) in self.bf:
                        print(
                            "Invalid move. Please try again.\n이동이 잘못되었습니다. 다시 시도해 주세요."
                        )
                        continue
                    break
                except ValueError:
                    print(
                        "Please enter a valid number between 1 and 9.\n1에서 9 사이의 유효한 숫자를 입력하세요."
                    )
        self.board = self.board.replace(block, player)
        if player == "X":
            self.x_score.append(int(block))
            player_score_list = self.x_score
        elif player == "O":
            self.o_score.append(int(block))
            player_score_list = self.o_score
        self.bf.append(int(block))
        new_board = self.board
        a = 1
        for i in self.board:
            while True:
                if a in self.bf:
                    a += 1
                else:
                    break
            if i == str(a):
                new_board = new_board.replace(i, " ")
                a += 1
        print(new_board)
        win = self.check_win(player_score_list)
        if win:
            self.ending(player)
            return False
        draw = self.check_draw()
        if draw:
            print(DRAW_TXT)
            return False
        return True

    def start_game(self):
        turn = "X"
        playing = True
        ai_game = input("1 = friend(친구), 2 = bot(봇)\n")
        if ai_game == "2":
            while True:
                human = input(
                    "What would you like to be, X or O?\nX 아니면 O 중에 뭐가 되고 싶나요?\n"
                )
                if human.upper() == "X":
                    self.o = "Bot"
                    break
                elif human.upper() == "O":
                    self.x = "Bot"
                    break
                else:
                    print(
                        "Invalid input. Please try again.\n잘못된 입력입니다. 다시 시도해 주세요."
                    )
            print(
                "To select a block, type the block number.\n블록을 선택하려면 블록 번호를 입력하세요."
            )
            while playing:
                playing = self.play_turn(turn)
                turn = "O" if turn == "X" else "X"
        elif ai_game == "1":
            print(
                "To select a block, type the block number.\n블록을 선택하려면 블록 번호를 입력하세요."
            )
            while playing:
                playing = self.play_turn(turn)
                turn = "O" if turn == "X" else "X"

        else:
            print("Invalid input. Please try again.\n잘못된 입력입니다. 다시 시도해 주세요.")
            self.start_game()

playing = True
while playing:
    game = Tic_Tac_Toe()
    game.start_game()
    continue_game = input("Again?\n다시?\n1=Yes(네) 2=No(아니요)\n")
    if continue_game != "1":
        playing = False
