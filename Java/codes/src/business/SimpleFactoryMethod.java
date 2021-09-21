package business;

import classes.IKeyboard;
import classes.MoonLanderKeyboard;
import classes.PlanckKeyboard;
import org.jetbrains.annotations.NotNull;

public class SimpleFactoryMethod {
    /**
     * Factory with Creator method.
     * This is a type of simple factory (the factory class directly defines creator method to instantiate
     * the required object)
     * @param type
     * @return
     * @throws Exception
     */
    public IKeyboard creator(@NotNull String type) throws Exception {
        if(type.equals("Planck")){
            return new PlanckKeyboard();
        }
        else if(type.equals("Monnlander")){
            return new MoonLanderKeyboard();
        }else {
            throw new Exception("Invalid Keyboard type");
        }
    }
}
