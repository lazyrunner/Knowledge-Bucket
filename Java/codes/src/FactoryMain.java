import business.SimpleFactoryMethod;
import classes.IKeyboard;

public class FactoryMain {

    public static void main(String[] args) throws Exception {

        System.out.println("Starting with simple factory method");
        SimpleFactoryMethod simpleFactory = new SimpleFactoryMethod();
        IKeyboard keyboard = simpleFactory.creator("Planck");
        System.out.println(keyboard.getType());

        System.out.println("Going to Factory Design pattern");


    }
}
