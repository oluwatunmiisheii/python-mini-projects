# Battle Simulator

![Battle Image](https://github.com/youruser/battle-simulator/assets/12345/battle-simulator-screenshot)

## What's this?

This is a simple Python program that simulates battles between different characters including zombies, ogres, and heroes. Players can equip heroes with weapons to increase their attack damage and watch the battles unfold in the terminal.

## How to Run

Make sure you have Python installed on your machine. You can download it [here](https://www.python.org/downloads/). Once you have Python installed, you can run the program by typing the following command in your terminal:

```bash
python3 main.py
```

## How to Use

Once the program is running, it's super easy to use! The simulation will automatically run:
* First, a battle between a zombie and an ogre
* Then, a battle between your hero (equipped with a weapon) and the remaining enemy

During battles, you'll see:
* Health points for each character
* Attack damage inflicted
* Special attack messages
* Battle outcomes showing who wins

## Game Elements

* **Enemies**: Zombies and Ogres with different health points and attack damage
* **Hero**: A player character that can be equipped with weapons
* **Weapons**: Items that increase the hero's attack damage
* **Battle System**: Turn-based combat with attacks and special abilities

## File Structure

* `main.py`: The main program file that runs the battles
* `zombie.py`: Contains the Zombie class implementation
* `ogre.py`: Contains the Ogre class implementation
* `hero.py`: Contains the Hero class implementation
* `weapon.py`: Contains the Weapon class implementation
* `enemy.py`: Contains the base Enemy class (parent class for Zombie and Ogre)