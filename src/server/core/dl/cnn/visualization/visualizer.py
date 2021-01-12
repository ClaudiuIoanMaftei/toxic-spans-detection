import matplotlib.pyplot as plt

class Visualizer:
    """
    Class - Visualizer
    Input:
    - words list
    - weights list
    Output:
    - 2D representation
    Feature:
    - the possibility of adding multiple weights lists
    """
    def __init__(self, words = [], weights = []):
        #
        print("[Visualizer] Initialising...")
        self.words = words
        self.words_weights = []
        if weights != []:
            self.words_weights.append(weights)

    def addData(self, weights):
        # Adding weights list
        self.words_weights.append(weights)

    def draw(self):
        # Function that deals with drawing
        print("[Visualizer] Drawing...")
        plt.xlabel('Words', fontsize=10, color='blue')
        plt.ylabel('Bad Duck Vibe', fontsize=10, color='red')
        plt.grid(True)
        plt.suptitle(' '.join(self.words))
        for line in self.words_weights:
            plt.scatter(self.words, line)
        plt.show()

if __name__ == "__main__":
    print("[DL Visualizer]")
    v = Visualizer(['cateodata','esti','ciudat'], [3, 3, 10])
    # v = Visualizer()
    v.addData([5, 1, 2])
    v.addData([1, 10, 23])
    v.draw()