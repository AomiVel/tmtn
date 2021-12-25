import discord,asyncio,inspect,os;
def print_line():print(inspect.currentframe().f_back.f_lineno)
b=os.environ.get('TOKEN');c=discord.Client(intents=discord.Intents.all())
@c.event
async def on_ready():
 print(len(c.guilds))
 print("Ready: {0.name} (ID: {0.id})".format(c.user))
def d(g):
 h={}
 for i in(g):
  if'twitter.com'not in(i.url):continue
  if(i.url)in(h.keys()):h[i.url].append(i)
  else:h[i.url]=[i]
 return(h)
def f(j):
 k=d(j);l={'a':False,'b':False,'c':False,'d':False}
 for m in(k.values()):
  if(len(m)==1):
   if(m[0].video):l['d']=True
  elif(len(m)==2):l['a']=True
  elif(len(m)==3):l['b']=True
  elif(len(m)==4):l['c']=True
 return(l)
q={'a':'<:two_image:922470315567775754>','b':'<:three_image:922470315332866058>','c':'<:four_image:922470315278336020>','d':'<:playable:922473752422400010>'}
@c.event
async def on_message(n):
 if(len(n.embeds)==0):
  try:_,a=await(c.wait_for('message_edit',check=lambda _,a:a.id==n.id,timeout=5));n=a
  except(asyncio.TimeoutError):return
  except(Exception)as e:return(print(e))
 o=f(n.embeds)
 for(p,r)in(o.items()):
  if(r):
   await(n.add_reaction(q[p]))
   await(asyncio.sleep(0.5))
@c.event
async def on_guild_join(_):
 print(len(c.guilds))
c.run(b)
