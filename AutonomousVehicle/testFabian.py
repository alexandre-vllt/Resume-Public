from robot_class import Robot

def nextStepToGotoGoal(self, x, y, direction, goal, whitePossiblePaths, obstacles):
        '''
        obstacles: liste de bool longueur 3: [y'a obstacle à gauche?, y'a obstacle au centre?, y'a obstacle à droite]
        '''
        possibleDirections = [0, 1, 2, 3]

        if self.direction in possibleDirections and (not whitePossiblePaths[1] or obstacles[1]):
            possibleDirections.remove(self.direction)
        if (self.direction - 1) % 4 in possibleDirections and (not whitePossiblePaths[0] or obstacles[0]):
            possibleDirections.remove((self.direction - 1) % 4)
        if (self.direction + 1) % 4 in possibleDirections and (not whitePossiblePaths[2] or obstacles[2]):
            possibleDirections.remove((self.direction + 1) % 4)
        
        # Déterminer dans quelle direction on devrait aller
        idealDirections = []
        if x != goal[0]:
            if x < goal[0]:
                idealDirections.append(1)
            else:
                idealDirections.append(3)
        if y != goal[1]:
            if y < goal[1]:
                idealDirections.append(2)
            else:
                idealDirections.append(0)
        
        correspondances = {direction: b'A',
                           (direction + 1) % 4: b'R',
                           (direction - 1) % 4: b'G',
                           (direction + 2) % 4: b'H'}
        
        print(idealDirections, possibleDirections)

        for direction in idealDirections:
            if direction in possibleDirections:
                return correspondances[direction]
        
        if possibleDirections:
            return correspondances[possibleDirections[0]]
    
        else:
            print('SITUATION IMPOSSIBLE !!!!!! Fabian ton code est pas bon')
        


robot = Robot(0, 0, 1, )
print(nextStepToGotoGoal(robot, 0, 0, 1, (0, 8), [False, True, False], [False, True, False]))