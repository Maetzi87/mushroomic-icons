![Downloads](https://img.shields.io/github/downloads/Maetzi87/mushroomic-icons/latest/total)
![Total Downloads](https://img.shields.io/github/downloads/Maetzi87/mushroomic-icons/total)
![Latest Release](https://img.shields.io/github/v/release/Maetzi87/mushroomic-icons)
![License](https://img.shields.io/github/license/Maetzi87/mushroomic-icons)
![Stars](https://img.shields.io/github/stars/Maetzi87/mushroomic-icons)

# 🍄 Mushroomic Icons

A standalone SVG icon set for Home Assistant, providing a clean and lightweight custom icon namespace `mushic:`.

The icons are especially designed to be used with [**Mushroomic Cards**](https://github.com/Maetzi87/lovelace-mushroomic-cards), but work anywhere in Homeassistant.

Mushroomic Icons mimic the style of the preinstalled Material Design Icons, adding Icons I personally missed. Some of the Icons are identical with mdi icons, but provide **auto-animation** in Mushroomic Cards.

All icons are automatically registered through the included mushic-icons.js bundle, making them globally available in Lovelace without any additional configuration.

---

## Available icons

<!-- ICONS START -->
<!-- ICONS END -->

---

## Install

### HACS

Add this repo via HACS as a plugin and install. See the [HACS install guide](./HACS_INSTALL.md) for step by step instructions.

### Manual

Copy the `music-icons.js` file into `<config>/www/` where `<config>` is your home-assistant config directory (the directory where your `configuration.yaml` resides).

Add the folowing to the `frontend` section of your `configuration.yaml`

```yaml
frontend:
  extra_module_url:
    - /local/mushic-icons.js
```

Or add the following to your lovelace configuration using the Raw Config editor under Configure UI or ui-lovelace.yaml if using YAML mode.

```yaml
resources:
  - type: js
    url: /local/mushic-icons.js
```

Restart home-assistant.

## Using

The icons uses the prefix `mushic:`.


## FAQ

Q: The icon ain't showing, it's just white space where it should be. What's up with that?

A: Probably related to cache. Try opening your instance in a incognito/private Window and see if your icon shows then. If yes, it's cache related. If not, spellcheck.
