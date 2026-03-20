# cache-redis-config
====================

## Description

A Node.js module for easy configuration of Redis in cache applications. It simplifies the process of connecting to Redis and managing cache configurations.

## Features

* Easy Redis connection setup
* Support for multiple Redis instances
* Automatic cache configuration
* Customizable cache settings
* Extensive error handling

## Technologies Used

* Node.js
* Redis
* JavaScript

## Installation

To install `cache-redis-config`, use npm:

```bash
npm install cache-redis-config
```

## Usage

```javascript
const { CacheRedis } = require('cache-redis-config');

const cache = new CacheRedis({
  host: 'localhost',
  port: 6379,
  db: 0,
  password: 'your_password',
});

// Get cache instance
const cacheInstance = cache.getInstance('my_cache');

// Set a value in the cache
cacheInstance.set('key', 'value');

// Get a value from the cache
const cachedValue = cacheInstance.get('key');
```

## Configuration

You can customize the cache configuration by passing options to the `CacheRedis` constructor.

```javascript
const cache = new CacheRedis({
  host: 'localhost',
  port: 6379,
  db: 0,
  password: 'your_password',
  maxConnections: 10,
  expire: 3600, // 1 hour
  failover: true,
  retryTimeout: 1000,
});
```

## Contributing

Contributions to `cache-redis-config` are welcome. Please submit a pull request or create an issue for any feature or bug fixes.

## License

`cache-redis-config` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Authors

* Your Name

## Acknowledgments

* Redis project team

## Changelog

See the [CHANGELOG](CHANGELOG.md) for a list of changes in each release.

## Issues

Report any issues to the [ISSUES](ISSUES.md) page.