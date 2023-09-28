"""
이 코드는 간단한 텍스트 기반 타워 디펜스 게임 프로젝트로, 플레이어는 몬스터를 막기 위해 타워를 배치하고 몬스터를 공격하는 전략적 게임을 플레이하는 것을 목표로 합니다. 
플레이어는 타워를 배치하고 업그레이드하며, 몬스터는 경로를 따라 이동하며 플레이어의 타워에 대항합니다. 
이 게임은 기본적인 게임 엔진 및 게임 루프, 그래픽 요소, 몬스터와 타워의 상호 작용을 포함하고 있으며, 게임 로직을 확장하거나 개선할 수 있는 기초를 제공합니다.
"""

# main.py

from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()