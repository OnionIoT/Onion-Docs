## Connecting to Cloud Platforms


In this section we would like to present our supported Cloud Platforms. The Omega can easily connect with with AWS IoT, Losant, Ubidots, IBM Watson IoT, Google Cloud IoT, and Blynk. Please continue reading to find out further details and instructions on how to get started and how to make your own Cloud connected project!

### AWS IoT

AWS (Amazon Web Services) IoT is a cloud platform that allows connected devices to interact with cloud applications, other devices, and other AWS services using an MQTT connection. It also implements a Device Shadow that can be used to store and retrieve a device's current state information, even when the device is offline. To read more about AWS IoT, please take a look at their [official documentation](https://aws.amazon.com/iot-core/).

We've made several tutorials on how to get your Omega up and running with AWS IoT. These tutorials include:

* [Single Command AWS IoT Setup](https://onion.io/2bt-aws-iot-setup-single-command/)
* [Pushing Sensor Data to Sensor Data to AWS IoT](https://onion.io/2bt-aws-iot-pushing-sensor-data/)
* [Visualizing Sensor Data on AWS](https://onion.io/2bt-aws-iot-visualizing-sensor-data/)


### Losant

[Losant](https://www.losant.com/) provides a very powerful and feature-rich IoT Cloud Platform. It’s a great fit for making your Omega projects flexible, customizable, and cloud-connected! With an emphasis on Enterprise solutions, you can use it as a testbed and then make the move to production.

Follow their [guide to connect your Omega2 to the Losant cloud platform](https://www.losant.com/blog/getting-started-with-omega2-and-losant) and then explore the various features they have to offer.

You can then explore our Smart Plant project that uses Losant to store and visualize sensor data from the Omega and then to instruct the Omega to perform actions based on the data. Refer to [Part 2 of the project](https://docs.onion.io/omega2-project-book-vol1/smart-plant-p2.html) that covers in depth how to set up an account with Losant, create an application and send data points from the Omega.

Once you've got familiar with their interface, you may want to go further by having Losant send commands to your Omega. Take a look at [Part 4 of the Smart Plant project](https://docs.onion.io/omega2-project-book-vol1/smart-plant-p4.html) that automates plant watering based on the reported soil moisture level.


### Ubidots

The [Ubidots Cloud platform](https://ubidots.com/) allows you to collect sensor data, process it, and create user-friendly data dashboards. See our [Ubidots tutorial](https://onion.io/2bt-pushing-data-to-the-ubidots-iot-platform/) to get an idea of how to connect your Omega with Ubidots.

You can also take a look at our [Ambient Temperature Monitor project](https://docs.onion.io/omega2-project-book-vol1/ubidots-temperature-monitor.html) for a detailed walkthrough of setting up a Ubidots device, connecting the Omega to Ubidots, and sending sensor data at an interval.


### IBM Watson IoT

The [IBM Watson IoT platform](https://internetofthings.ibmcloud.com/) makes it easy to manage your device, collect, store, and visualize data, and make use of other IBM services. Follow along with their [community recipe](https://developer.ibm.com/recipes/tutorials/connect-an-onion-omega2-to-ibm-watson-iot-platform/) to learn how to connect your Omega to the IBM Watson IoT Platform.

Check out our [Weather Station](https://docs.onion.io/omega2-project-book-vol1/weather-station.html) project for a detailed walkthrough on building an IoT project that will transmit sensor data to Watson IoT and how to visualize that data.

### Google Cloud IoT Core

The [Google Cloud IoT Core](https://cloud.google.com/iot-core/) is a fully managed service to easily and securely connect, manage, and ingest data from globally dispersed devices. In combination with other services on Google Cloud IoT platform, Google Cloud IoT provides a solution for collecting, processing, analyzing, and visualizing IoT data in real time to support improved operational efficiency.

Follow along with [this community-made tutorial](https://onion.io/2bt-may-29-2018/) to learn how to setup two-way MQTT communication with Google Cloud IoT Core using the mosquitto utility. For background on creating a Device on Google Cloud, see their [Creating Registries and Devices  Tutorial](https://cloud.google.com/iot/docs/how-tos/devices). Also see [this Medium post](https://medium.com/google-cloud/google-cloud-iot-core-golang-b130f65951ba) detailing how to write a GoLang program that establishes a connection with Google Cloud IoT and receives as well as sends data.

### Blynk

With Blynk, you can control your IoT device, in this case the Omega2, with your smartphone! Install Blynk's NodeJS library on your Omega and you'll be good to go. See our [walkthrough on using Blynk](https://onion.io/2bt-blynk-omega/) for an example of how to control your Omega with the Blynk App. For more information you can visit the [Blynk website](https://www.blynk.cc/).
