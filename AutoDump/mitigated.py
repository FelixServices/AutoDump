from dhooks import Webhook, Embed

embed = Embed(
        description='**Attack has been detected for:**\n``VeteranVPN Canada OVH-GAME``\n\n**Server Provider:**\n``OVH Hosting``\n\n**Location:**\n``Canada, US``\n\n**Attack successfully mitigated the OVH has been withdrawn from the mitgation infrastructure**',
        color=0xfafcfa,
        timestamp='now'
        )

embed.set_thumbnail('https://www.seekpng.com/png/full/205-2059350_safe-black-and-white-verified.png')
embed.set_footer(text="Attack Mitigated")

hook = Webhook('https://discord.com/api/webhooks/894757651223822347/a2TRRca5ylOHxoO0squg7PVXd22wEz-8uHm8wKJ1MO8YUHf174a8f09TuOHFzn71I2tm')

hook.send(embed=embed)
