# AutoGPT_IFTTT.
A webhook connector for If-This-Then-That

### Plugin Installation Steps

1. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

2. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ``` shell
   ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3
   ```

###   Connect the .ENV
Add this to your .env to get AutoGPT to send to the right endpoint.
```
################################################################################
### AUTOGPT IFTTT Webhook Integration
################################################################################
IFTTT_WEBHOOK_TRIGGER_NAME=<your trigger is here>
IFTTT_KEY=<your key goes here>

```

###   Set up IFTTT
IFTTT requires a webhooks connector. Create a new applet or modify an existing one, and Webhooks to the applet. Set up a trigger name that you won't forget; 
this trigger will be how you get the call into IFTTT. Above it is your ```IFTTT_WEBHOOK_TRIGGER_NAME```

Once added, you'll have to go to the documentation button to find your specific key. The key will route your json content to you will be posting.

### Processing the data
Once the first post works, you'll have a JSON value going into IFTTT. use a javascript filter to make decisions about your content.

In this example, if I don't have anything worth doing, don't send em an email.

```
let payload = JSON.parse(MakerWebhooks.jsonEvent.JsonPayload)

if (payload.data != null)
{  
  let title = payload.data[0].title
  let summary = payload.data[0].summary
  let content = payload.data[0].content

  if (summary === "undefined")
    Email.sendMeEmail.skip("No content was found")
  else
    Email.sendMeEmail.setSubject(title)
    Email.sendMeEmail.setBody("Summary:" + summary + "\n\nContent: " + content)
}
else
  Email.sendMeEmail.skip("No data was found");
```

###   TEST IT
Good luck!
