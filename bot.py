from random import randint

class Bot():
    def __init__(self) -> None:
        self.winning_list = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

    def check_almost_win(self, score, blocks_played):
        for combo in self.winning_list:
            if sum(num in score for num in combo) == 2 and [num for num in combo if num not in score and num not in blocks_played]:
                missing_num = [num for num in combo if num not in score]
                return {"almost_win":True, "combo":combo, "missing_num":missing_num}
        return {"almost_win":False, "combo":None}
    
    def random_number(self, blocks_played):
        while True:
            random_block = randint(1,9)
            if random_block not in blocks_played:
                return random_block

    def make_move(self, blocks_played, ops_moves, own_moves):
        almost_win = self.check_almost_win(ops_moves, blocks_played)
        almost_own_win = self.check_almost_win(own_moves, blocks_played)
        if almost_own_win["almost_win"]:
            missing_numb = str(almost_own_win["missing_num"][0])
            return missing_numb
        else:
            if almost_win["almost_win"]:
                missing_numb = str(almost_win["missing_num"][0])
                print(missing_numb)
                return missing_numb
            else:
                
                random_play = self.random_number(blocks_played)
                return str(random_play)

