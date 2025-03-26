import os
import discord
from discord.ext import commands
from myserver import server_on


# 🔹 กำหนด Prefix คำสั่ง (เช่น ! หรือ ?)
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ บอท {bot.user} ออนไลน์แล้ว!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"👋 สวัสดี {ctx.author.mention}!")

@bot.command()
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(f"🧮 ผลลัพธ์: {a} + {b} = {result}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "สวัสดี" in message.content:
        await message.channel.send(f"👋 สวัสดี {message.author.mention}!")
    await bot.process_commands(message)  # สำคัญ! ให้คำสั่งอื่นทำงานได้

@bot.command()
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🗑️ ลบข้อความ {amount} ข้อความแล้ว", delete_after=3)

"""
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="ไม่มีเหตุผล"):
    await member.ban(reason=reason)
    await ctx.send(f"🚫 แบน {member.mention} ออกจากเซิร์ฟเวอร์ (เหตุผล: {reason})")
"""
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="ข้อมูลเซิร์ฟเวอร์", description="นี่คือเซิร์ฟเวอร์ของเรา!", color=0x00ff00)
    embed.add_field(name="👥 สมาชิก", value=f"{ctx.guild.member_count} คน")
    embed.set_footer(text="Powered by Discord Bot")
    await ctx.send(embed=embed)

server_on()

bot.run(os.getenv('TOKEN'))
