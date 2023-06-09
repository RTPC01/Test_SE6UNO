import pygame

# 색 카드 추가를 위한 리승트
colors = ['red', 'green', 'blue', 'yellow']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'skip', 'reverse', 'draw_2', 'bomb', 'one_more']


# 색약 모드 옵션을 위한 임시값 (추후 삭제)
class Option:
    def __init__(self, color_weakness):
        self.color_weakness = color_weakness


# Option 클래스를 인스턴스화합니다.
option = Option(False)


class Card:
    def __init__(self, color, value, card_img, card_img_back):
        self.color = color  # 색
        self.value = value  # 숫자
        self.card_img = card_img  # 플레이어가 볼 자신의 카드 이미지
        self.card_img_back = card_img_back  # 상대방 에게 보여질 카드 뒷면

    def __str__(self):
        return f"{self.color} {self.value}"

    def __repr__(self):
        return self.__str__()

    def is_special(self):
        return self.value in ["skip", "reverse", "draw_2", "bomb", "one_more", "shield", "change"]


def resize_image(image, scale_percent):
    width = int(image.get_width() * scale_percent / 100)
    height = int(image.get_height() * scale_percent / 100)
    return pygame.transform.scale(image, (width, height))


def generate_cards():
    cards = []
    card_back_image_big = pygame.image.load("resources/Image/card_images/card_back.png")
    card_back_image = resize_image(card_back_image_big, 10)

    card_folder = "resources/image/cw_card_images" if option.color_weakness else "resources/image/card_images"
    # 색약 모드와 경로 차별화

    for i in range(2):
        for color in colors:
            for value in values:
                card_image = pygame.image.load(f"{card_folder}/{color}_{value}.png")
                card_image_resized = resize_image(card_image, 10)  # 이미지 크기를 5%로 조정합니다.
                card = Card(color, value, card_image_resized, card_back_image)
                cards.append(card)

    # 색 없는 실드카드를 한 번에 추가합니다.
    for i in range(2):
        card_image = pygame.image.load(f"resources/Image/card_images/none_shield.png")
        card_image_resized = resize_image(card_image, 10)  # 이미지 크기를 5%로 조정합니다.
        card = Card('none', 'shield', card_image_resized, card_back_image)
        cards.append(card)

    # 색 없는 색변경 카드를 추가
    for i in range(2):
        card_image = pygame.image.load(f"resources/Image/card_images/none_change.png")
        card_image_resized = resize_image(card_image, 10)  # 이미지 크기를 5%로 조정합니다.
        card = Card('none', 'change', card_image_resized, card_back_image)
        cards.append(card)
    return cards


'''
# 카드 살펴보기 (추후 삭제)
def print_cards(cards):
    for card in cards:
        print(f"Color: {card.color}, Value: {card.value}, Card Image: {card.card_img}, Back: "f"{card.card_img_back}")
        print(f"Is the card special? {card.is_special()}")


if __name__ == "__main__":
    cards = generate_cards()
    print_cards(cards)
'''