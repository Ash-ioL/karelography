import kareltherobot.*;

public class App implements Directions {
    
    static {
        World.setDelay(30);
        World.setVisible(true);
    }
    
    public static void main(String[] args) throws Exception {
        Robot bot1 = new Robot(1, 1, East, 2);
        for (int i = 0; i < 5; i++) {
            bot1.move();
        }
        bot1.pickBeeper();
        bot1.move();
        bot1.turnOff();
    }
}
