name = input("Type your name: ")
print("Welcome, ", name, "to your walk to Silverburn")

answer = input("You are outside your own house facing Silverburn. long or short route? ").lower()

if answer == "long":
    answer = input("You leave your house and walk down Corsford drive towards the burn. You can go left towards the triangle or right, up the stairs and down the lane. Left or Right? ").lower()

    if answer == "left":
        answer = input("You walk around the corner, by the triangle and come to brock road. You can go right, along Brock Road, or continue towards Househilmuir Crescent. right or continue? ").lower()
        #right
        if answer == "right":

            answer = input("You walk along the Brock road towards Silverburn. At the end of the Brock road you have 2 options. Go left towards the zebra crossing. Or jump the fence and cross straight away. Left or Jump? ").lower()
            if answer == "left":
                print("You make your way towards the zebra crossing and make it safely across. You have made it to Silverburn.")
            elif answer == "jump":
                print("You leap like a gazelle over the waist high fence and trip. the X8 on its way to Ayr runs over your head and pops your wee heid like a balloon. Should've gone left.")
            else:
                print("Not a valid option")
        #continue
        elif answer == "continue":
            answer = input("You continue towards Househilmuir Crescent and have 2 options. Left, towards househilmuir road, or right, towards Silverburn. Left or Right? ").lower()
            if answer == "left":
                print("A random skip falls out of the sky right in front of you causing you to leap backwards into the path of a lion thats escape from a nearby zoo(govan). It eats you alive and lives happily ever after. The End.")
            elif answer == "right":

                answer = input("You go right, walking along Househilmuir Crescent, pass Househilmuir Place, which connects to Househilmuir Road, and you come to the Zebra crossing at Cowglen Road. Do you wait for traffic to clear, or dash across with not a care in the world. Wait or Dash? ").lower()
                if answer == "wait":
                    print("As you wait, a lamp post falls on you and squashes you. Should've lived life to the max, to hell with waiting.")
                elif answer == "dash":
                    print("You dash and make it safely across. Congratulations, you've arrived at Silverburn")
                else:
                    print("Not a valid option")

            else:
                print("Not a valid option")
        else:
            print("Not valid option")

    elif answer == "right":
        answer = input("You make your way up the stairs and go left, towards Silverburn along the lane. You remember a time when you could jump the burn but the tree's are all overgrown and your old to boot. Eventually, you come to the end of the lane. You can jump the fence or go right towards the crossing. Jump or Right? ").lower()
        if answer == "jump":
            print("As you jump you pull a hamstring and tear your trousers. You're really quite old so jumping the fence was really really really really daft. You limp home, hoping nobody noticed your failed adventure.")
        elif answer == "right":
            answer = input("You walk around the corner, past the weird statue from the old Pollok Centre, and come to the crossing. You can walk straight across with no regard for your personal safety or wait until traffic clears because, dammit, that milk and bread isn't going to buy itself. Walk or Wait? ").lower()
            if answer == "walk":
                print("You take the chance and walk straight out into traffic. Like an optical illusion you blend between the traffic like Neo from the Matrix. As you arrive on the other side of the road, outside Silverburn, you reflect on a lovely walk and look forward to some lovely bread on milk. I don't drink milk so i assume you pour it on the bread right?")
            elif answer == "wait":
                print("Are you insane? As you wait for traffic to clear outside one of the busiest roads on Earth, the mighty Cowglen Road, the heat death of the universe arrives which means that the bread you were going to buy is now out of date. Muppet.")
            else: 
                print("Not a valid option")
        else:
            print("Not a valid option")

    else:
        print("Not a valid options")

elif answer == "short":
    answer = input("You go right, walking up Priesthill Crescent. You come to Plenshin Court. Do you want to go left, towards Silverburn, or continue along Priesthill Crescent? Left or Continue? ").lower()
    if answer =="left":
        answer = input("You go left, down Plenshin Court. You come to the lane that takes you to silverburn. Do you go left, down the lane, or continue along Plenshin Court? Left or Continue? ").lower()
        if answer == "left":
            answer = input("You go left, walking down the lane towards Silverburn, past the flood overflow protections and across the road, over the bridge across the Burn. You come to the single lane, 30 mph, Cowglen Road that is quiet at this time of day. At the crossing a car has slowed and is waiting for you to cross. Do you cross as instructed, or ignore the car and pretend you didn't see the driver's intent? Cross or Wait? ").lower()
            if answer == "cross":
                print("You decide to cross as instructed, doing your best to both acknowledge the gesture and check both ways as you cross the road. As your crossing another car is coming in the opposite direction and doesn't slow. It keeps going and you cross safely after its gone. Both of these things took the same amount of time but for some reason one of the cars decided to stop and try and communicate with a pedestrian that they could cross. Please stop doing this drivers. Let me decide when to cross, you concentrate on driving. Whatever, you've arrived at Silverburn and will now spend a stupid amount of time trying to figure out if your acknowledgment to the driver was awkward and will prevent you from going to sleep at night as you re-evaluate your social and life skills.....or you're a normal person and just forget it as soon it happens. The END!")
            elif answer == "wait":
                print("Not noticing that you have decided to ignore their instruction. The car that has slowed, continues to wait. After a while the driver decides to just continue driving, giving you a nasty look as you continue to look everywhere but at the car. With the car gone, you cross the road into Silverburn. Please FOR THE LOVE OF GOD STOP SLOWING DOWN TO LET PEDESTRIANS CROSS ON LOW TRAFFIC VOLUME ROADS. IT JUST CAUSES MORE PROBLEMS ESPECIALLY AS THE PERSON WALKING HAS MORE THAN 1 LANE OF TRAFFIC TO WORRY ABOUT AND NOW THEY NEED TO WORRY ABOUT UPSETTING THE PERSON WHO HAS SLOWED TO DO SOMETHING THEY THINK IS A NICE GESTURE. IN THE NAME OF THE WEE MAN JUST KEEP DRIVING, IM NOT CROSSING A DUAL CARRIAGE WAY HERE. Jesus.")
            else:
                print("Not a valid option")
        elif answer == "continue":
            print("You continue down plenshin court and realise it's a cul de sac with a roundabout in the middle. You walk around the roundabout and return to where you started at the lane towards silverburn. Well done, you've wasted my time and yours.")
        else:
            print("Not a valid option")
    elif answer == "continue":
        print("This entire program is taking way too long to do, seriously it's like 80 lines of code. So here the rest of the program for short. You can walk along Priesthill Crescent until you come to Kaim Drive. You can walk down Kaim Drive and then go straight ahead, across the road and walk along the burn. You can also stay on the main road by going left and continue down until you come to the lane on your left. You can't walk up the lane but you can turn right and walk across the bridge, across the burn and come to the Cowglen Road outside Silverburn. If you didn't walk down Kaim Drive, you would be taken up Priesthill Crescent, left, along Priesthill Road and then Left again down Muirshiel Crescent. You would walk down this road until you came to Kaim Drive and be presented with the same options as before, before arriving at Cowglen Road. At this point there would be a range of hilarious things for you to do but I've alreay spent way to long on this. It's to move on. Thanks for playing,", name)
    else:
        print("Not a valid option")
else:
    print("Not a valid option")


print("Thanks for playing", name)