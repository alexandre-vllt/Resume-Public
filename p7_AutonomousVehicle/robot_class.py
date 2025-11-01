'''
Classe du robot
'''

state_list = ['suivi_de_ligne' ,'fail', 'obstacle', 'intersection']


class Robot():
    def __init__(self, x_start, y_start, initial_dir, mission ='huit', state = 'suivi_de_ligne', priority = ['A','R','L']) -> None:
        self.x = x_start
        self.y = y_start
        self.enLivraison = True
        
        if initial_dir == 0:
            self.y -= 1
        elif initial_dir == 1:
            self.x += 1
        elif initial_dir == 2:
            self.y += 1
        elif initial_dir == 3:
            self.x -= 1
        
        self.x_home = x_start
        self.y_home = y_start
        self.direction = initial_dir # nombre entre 0 et 3: 0 = haut, 1 = droite, 2 = bas, 3 = gauche
        self.curretlyAdjustingXorY = 'x'
        self.goal = None
        self.intersection_priority = priority
        self.mission = mission
        if state in state_list:
            self.state = state
        else:
            print('[ERROR] Mission inconnue')
            self.state = 'fail'
    
    def direction_choice(self, possible_directions):
        '''directionIndex = {'L':0, 'A' : 1, 'R' : 2}
        for X in self.intersection_priority:
            if possible_directions[directionIndex[X]]:
                return X'''
        return b'A'
            
    
    def switch_status(self, new_status):
        '''
        Change le statut du robot
        '''
        if new_status in state_list:
            self.state = new_status
        else :
            print('[ERROR] Mission inconnue')
            self.state = 'fail'
        
        if self.state == 'intersection':
            self.set_intersection_priority()
            
    def set_intersection_priority(self):
        pass
    
    def goal_definition(self,x_goal,y_goal):
        '''
        Definition de l'objectif (pour l'instant juste des coordonnees)
        '''
        self.goal = (x_goal,y_goal)
        
    def check_arrive(self):
        '''
        Verifie si le robot est arrive a son objectif
        '''
        return (self.x,self.y) == self.goal
    
    def return_to_home(self):
        '''
        Lance le retour a la maison
        '''
        self.goal_definition(self.x_home, self.y_home)
        self.enLivraison = False


    @staticmethod
    def convertDirectionIntToVector(direction):
        if direction == 0:
            return (0, -1)
        elif direction == 1:
            return (1, 0)
        elif direction == 2:
            return (0, 1)
        elif direction == 3:
            return (-1, 0)

    def moveBy(self, vector):
        self.x += vector[0]
        self.y += vector[1]

    def getLeftDirectionInt(self):
        return (self.direction - 1) % 4

    def getRightDirectionInt(self):
        return (self.direction + 1) % 4

    
    # Fabian
    def nextStepToGotoGoal(self, whitePossiblePaths, obstacles):
        '''
        obstacles: liste de bool longueur 3: [y'a obstacle à gauche?, y'a obstacle au centre?, y'a obstacle à droite]
        '''
        possibleDirections = [0, 1, 2, 3]

        if self.direction in possibleDirections and (not whitePossiblePaths[1] or obstacles[1]):
            possibleDirections.remove(self.direction)
        if self.getLeftDirectionInt() in possibleDirections and (not whitePossiblePaths[0] or obstacles[0]):
            possibleDirections.remove(self.getLeftDirectionInt())
        if self.getRightDirectionInt() in possibleDirections and (not whitePossiblePaths[2] or obstacles[2]):
            possibleDirections.remove(self.getRightDirectionInt())
        
        # Déterminer dans quelle direction on devrait aller
        
        if self.x == self.goal[0] and self.y == self.goal[1]:
            if self.enLivraison == False:
                return
            self.return_to_home()

        
        idealDirections = []
        if self.x != self.goal[0]:
            if self.x < self.goal[0]:
                idealDirections.append(1)
            else:
                idealDirections.append(3)
        if self.y != self.goal[1]:
            if self.y < self.goal[1]:
                idealDirections.append(2)
            else:
                idealDirections.append(0)

        
        finalDirectionIntChoice = None
        
        for direction in idealDirections:
            if direction in possibleDirections:
                finalDirectionIntChoice = direction
                break
        
        else:
            if possibleDirections:
                finalDirectionIntChoice = possibleDirections[0]
            
        #print(f'corresopndances, {correspondances}')
        print(f'ideal directions {idealDirections}, possibleDirections {possibleDirections}')
        print('CURRENT POS', (self.x, self.y), self.direction, self.goal)
        if finalDirectionIntChoice is None:
            print('[ERROR] SITUATION IMPOSSIBLE !!!!!! Fabian ton code est pas bon')
            return None
        else:
            
            if finalDirectionIntChoice == self.direction:
                finalDirectionLetter = b'A'
            elif finalDirectionIntChoice == self.getRightDirectionInt():
                finalDirectionLetter = b'R'
            elif finalDirectionIntChoice == self.getLeftDirectionInt():
                finalDirectionLetter = b'L'
            elif finalDirectionIntChoice == (self.direction + 2) % 4:
                finalDirectionLetter = b'H'
                
            self.direction = finalDirectionIntChoice
            self.moveBy(self.convertDirectionIntToVector(finalDirectionIntChoice))
            
            return finalDirectionLetter
        


        
