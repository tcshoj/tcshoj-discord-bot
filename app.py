import os
import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('哇！'):
        await message.channel.send(
            '雪莉？:flushed: 哇！:open_mouth::open_mouth: 珍妮佛羅培茲！:open_mouth::open_mouth: 你剛剛攻擊我的村莊？:rage::rage: 我的 Coin Master 村莊？:rolling_eyes::rolling_eyes: 呃 :astonished: 應該是吧？:sweat_smile::sweat_smile: 酷欸 :sunglasses::sunglasses::sunglasses: 你大老遠跑來這裡就因為我攻擊你的村莊？:rage: 我我我...我也 :point_right_tone1: :point_left_tone1: 為此而來！:pineapple::pineapple::joy::joy::joy::fire::fire::fire:')

    if message.content.startswith('笑死'):
        await message.channel.send(
            '笑死:joy::joy::joy::thumbsup::thumbsup:這你自己想出來的嗎:flushed::flushed:很厲害欸:sunglasses::sunglasses: 哈哈是我啦你是不是很懂嘻哈啊skrskr:call_me::call_me::call_me::sunglasses::sunglasses::sunglasses::punch::punch::punch::middle_finger::middle_finger::middle_finger::vulcan::vulcan::vulcan: peace 笑死:joy::joy::joy::thumbsup::thumbsup:這你自己想出來的嗎:flushed::flushed:很厲害欸:sunglasses::sunglasses:')

    if message.content.startswith('超跑'):
        await message.channel.send(
            """轟隆隆隆:rofl::rofl:隆隆隆隆衝衝衝衝:smirk::smirk::smirk:拉風:sunglasses::sunglasses::sunglasses:引擎發動:key::key::key:引擎發動+:red_car:+:point_right:+:red_car:一瞬間踩下油門:race_car::dash::dash:催乎盡磅(台):triumph::triumph:乘風:dash:衝:rofl:衝:rofl:讓窗外的:loudspeaker::loudspeaker:風 :dash::dash: 吹動每一個毛孔:woman:🦲:bearded_person: 我是今夜:crescent_moon::crescent_moon: 最:sunglasses: 稀有的品種:nerd::nerd: 讓:hushed: 看到的人以為是夢:scream::scream: 還沒醒來:sleeping::sleeping: 就已經無影無蹤:ghost::ghost: 風 :dash::dash: 敲醒每一個面孔:astonished::astonished: 我是明天:call_me::call_me: 被 贊嘆的驚悚:dizzy_face::dizzy_face: 讓:fearful::fearful: 看到的人全部感動:sob::sob: :zero:到:100:K only :four:秒鐘:smirk::smirk:""")


client.run(os.environ["BOT_TOKEN"])
