# AutoGPT_IFTTT
A webhook connector for If-This-Then-That (IFTTT) using the Auto-GPT framework. This plugin allows you to easily integrate IFTTT with the powerful language model GPT-4 to create various automations and applications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Plugin Installation Steps](#plugin-installation-steps)
- [Connect the .ENV](#connect-the-env)
- [Set up IFTTT](#set-up-ifttt)
- [Processing the data](#processing-the-data)
- [Testing](#testing)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have the following:

- Auto-GPT repository
- An IFTTT account

## Plugin Installation Steps

1. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

2. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ```shell
   ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3
   ```

## Connect the .ENV

Add this to your .env to get AutoGPT to send to the right endpoint.

```
################################################################################
### AUTOGPT IFTTT Webhook Integration
################################################################################
IFTTT_WEBHOOK_TRIGGER_NAME=<your trigger is here>
IFTTT_KEY=<your key goes here>
```

## Set up IFTTT

IFTTT requires a webhooks connector. Create a new applet or modify an existing one, and add Webhooks to the applet. Set up a trigger name that you won't forget; 
this trigger will be how you get the call into IFTTT. Above it is your ```IFTTT_WEBHOOK_TRIGGER_NAME```

Once added, you'll have to go to the documentation button to find your specific key. The key will route your json content to you will be posting.

## Processing the data

Once the first post works, you'll have a JSON value going into IFTTT. Use a JavaScript filter to make decisions about your content.

In this example, if I don't have anything worth doing, don't send me an email.

```javascript
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

## Testing

To test the integration, perform the following steps:

1. Send a sample request to AutoGPT
2. Verify that the request is received by IFTTT
3. Check the processing logic and ensure it is working as expected

## Usage

After successful testing, you can start using this plugin to create various automations and applications with the help of the GPT-4 language model and IFTTT.

## Troubleshooting

If you encounter any issues while using the plugin, refer to the following:

- Check the `.env` file for proper configuration.
- Verify that the IFTTT webhook trigger name and key are correct.
- Inspect the IFTTT applet configuration and ensure it is set up properly.
- Review the JavaScript filter for any syntax errors or logical issues.
- Check the Auto-GPT logs for any errors or warnings related to the plugin.

## Contributing

We welcome contributions to the AutoGPT_IFTTT plugin! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes, ensuring they adhere to the project's coding standards and guidelines.
4. Submit a pull request with a detailed description of your changes.

Please note that by contributing to this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).
