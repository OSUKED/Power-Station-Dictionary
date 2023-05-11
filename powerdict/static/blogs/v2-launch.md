---
title: "Building the New Power Station Dictionary: A Comprehensive and Dynamic Energy Data Platform"
date: 2023-04-26
authors:
  - Ayrton Bourn
description: Announcing major upgrades to the Power Station Dictionary, transforming it into a dynamic, user-driven platform that makes it easier to link datasets and promotes collaboration within the energy data community.
---

Access to accurate and comprehensive data is essential for informed decision-making and effective policy development in the rapidly evolving energy landscape. Despite numerous efforts to increase the visibility of energy data, challenges still persist due to the fragmentation and lack of standardisation in the data landscape. The Power Station Dictionary, first introduced over a year ago, aimed to address these issues by providing a platform for mapping between various power plant identifiers and automatically extracting data from Frictionless Data packages.

We’ve received some great feedback on the first version of the Power Station Dictionary, and we’re currently working on many of those suggestions as part of a new release. We are excited to announce several major upgrades to the Power Station Dictionary, transforming it into a dynamic, user-driven platform that makes it easier to link datasets and promotes collaboration within the energy data community.

Upgrades and Enhancements

1. Integration of SQLModel and Frictionless Data: The new Power Station Dictionary will feature a set of SQLModel schemas for validating Frictionless Data metadata and automatically saving both the metadata and raw data into a SQL database. This enables us to add datasets on the fly without needing to rebuild the website.
2. Transition to a Database-Driven Backend: The existing Power Station Dictionary will be moved into a database, allowing for more seamless integration of data from various sources. This will facilitate the addition of new source datasets and enable the platform to better manage the energy data it hosts and scale with larger datasets.
3. Introduction of a Dynamic Website: By employing a FastAPI app for serving Frictionless Data metadata and raw datasets, the Power Station Dictionary website will become more dynamic, with templates rendered on the fly from the database. This will not only improve the user experience but also enhance the overall functionality of the platform.
4. User Authentication and Collaboration Features: The updated Power Station Dictionary will introduce user authentication, enabling users to contribute and collaborate on the platform. Users will be able to link new IDs, add new power stations to the dictionary, and track their contributions, encouraging data sharing among energy professionals.
5. Enabling Data Growth: The Power Station Dictionary will now allow users to add new link types and Frictionless Data packages, facilitating the growth of the platform's data resources. The website will update automatically upon the addition of new datasets or links, ensuring that users have access to the most up-to-date information available.

The upcoming release of the Power Station Dictionary marks a significant milestone in the evolution of the platform. By introducing a dynamic and collaborative environment, we hope to empower users to contribute to the platform's growth, strengthening the energy data ecosystem and providing valuable insights to drive progress in the energy sector. We invite you to join us on this exciting journey as we continue to enhance and expand the Power Station Dictionary.