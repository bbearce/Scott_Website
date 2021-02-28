from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return """
<h2>RECIPE</h2>

<i>Medical disclaimer</i>

<p>This is the guide for your more stress free future.</p>
<p>The cure to negative Addiction is not impossible. It is a recipe.</p>
<p>The recipe contains tips on how to heal the mind as properly and peacefully as possible with a fraction of the pain that comes with traditional detoxing.-The most valuable ingredient is wanting and having the will to try to quit.</p>

<p>However, even if you don’t have the will to quit, it’s important to learn the information for when the time comes when you have no choice but to try to quit. Thus, here at ucureu know how hard this can be and appreciate you for learning. It is vital to keep in mind that with addiction, breakdown is not the end. If you believe you have failed with this program, remember this is not true. You have discovered precious abilities and tricks to help you achieve success in the future.</p>

<p>The recipe:</p>
<ul>
    <li>Read the pamphlet of questions and statements aloud several times. Reflecting and trying to align your intentions with the intentions of the writing is key.</li>
    <li>Proceed to crush 4-6 grams of Mushrooms into a pulverized powder and add the contents to a clean and drink the tea</li>
    <li>Continue to read the pamphlet aloud. This will help open your mind to new possibilities.</li>
    <li>Play Mozart music USING HEADPHONES and relax until you fall asleep.</li>
    <li>It is important to realize that taking this dose may intensify the feeling of hopelessness and addiction while under the influence. However, it’s vital to remember that after you wake up, you will feel much better. It will be similar to condensing 20 days worth of cravings into 1 experience.</li>
    <li>Be certain that you are in a safe and clean environment. If you are uncomfortable, cannabis may help you relax during this step.</li>
    <li>Remember that who you are in the past does not have to match the future you.</li>
    <li>Exercise daily from now on. It will allow you to experience a natural high.</li>
    <li>Refrain from using harmful addictions as best you can from now on.</li>
    <li>wait less than 10 days to administer doses</li>
</ul>

<p>Repeat these steps every 3-10 days for 3 more times. A higher dose of mushrooms will be required if you 
If you can’t have the belief that you are capable of quitting, try to focus your attention on disliking the substance. Try to realize how hollow it is. Remember how much energy, time, money, and respect it can cost and how it never gets better. Say aloud “I hate my addiction” several times each day and whenever you have a craving. After some time of doing this repeatedly, you will form the belief that you’re capable of quitting.</p>
"""
