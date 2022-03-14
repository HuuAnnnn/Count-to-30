import math

class Counting_AI:
    def __init__(self):
        pass
    
    def is_finish(self):
        return len(self.__curr_state) == 30

    def is_win(self, num_list):
        return 30 in num_list
    
    def __is_lose(self, num_list):
        return num_list[-1] == 29

    def evaluation(self, state, depth):
        if state == 'Win':
            return 1 + depth
        elif state == 'Lose':
            return -1 - depth
        else:
            return None

    def __generate_num_list(self, start, num_range):
        return [num for num in range(start+1, start + num_range + 1)]

    def __check_state(self, num_list):
        if self.is_win(num_list):
            return 'Win'
        elif self.__is_lose(num_list):
            return 'Lose'
        else:
            return None

    def __minimax(self, num_list, depth, is_maximize, alpha, beta):
        current_state = self.__check_state(num_list)
        if current_state:
            return self.evaluation(current_state, depth)
        
        if is_maximize:
            best_score = -math.inf
            for i in range(1, 4):
                move = self.__generate_num_list(num_list[-1], i)
                score = self.__minimax(move, depth + 1, False, alpha, beta)
                best_score = max(best_score, score)
                alpha = max(best_score, alpha)
                if beta <= alpha:
                    break

            return best_score
        else:
            best_score = math.inf
            for i in range(1, 4):
                move = self.__generate_num_list(num_list[-1], i)
                score = self.__minimax(move, depth + 1, True, alpha, beta)
                best_score = min(best_score, score)
                beta = min(best_score, beta)
                if beta <= alpha:
                    break

            return best_score

    def __best_move(self, human_num_list):
        best_num_list = []
        start_point = human_num_list[-1]
        best_score = -math.inf
        for i in range(1, 4):
            move = self.__generate_num_list(start_point, i)
            score = self.__minimax(move, 0, False, -math.inf, math.inf)
            if score > best_score:
                best_score = score
                best_num_list = move                
            
        return best_num_list
    def ai(self, human_num_list):
        return self.__best_move(human_num_list)