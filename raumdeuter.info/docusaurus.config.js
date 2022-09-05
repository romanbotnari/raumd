// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'raumd',
  tagline: 'Your python based shell spaceship',
  url: 'https://github.com/romanbotnari/raumd',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'romanbotnari', // Usually your GitHub org/user name.
  projectName: 'raumd', // Usually your repo name.

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'raumd',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            to: '/about',
            position: 'left',
            label: 'about',
          },
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'docs',
          },
          {
            to: 'https://airlocks.xyz',
            position: 'left',
            label: 'airlocks.xyz',
          },
          {
            href: 'https://github.com/romanbotnari/raumd',
            label: 'github',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Docs',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Discord',
                href: 'https://discord.com/channels/994139227950420019/994139228986425446',
              }
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'airlocks.xyz',
                to: 'https://airlocks.xyz',
              }
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} raumd.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
