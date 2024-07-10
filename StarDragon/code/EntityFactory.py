from code.Background import Background
from code.Const import WIN_WIDTH

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position= (0, 0)):
        if entity_name == 'Level1Bg':
            List_Bg = []
            for i in range (7):
               List_Bg.append(Background(f'Level1Bg{i}', (0, -300)))
               List_Bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, -300)))
            return List_Bg
