import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/about/',
    component: ComponentCreator('/about/', '608'),
    exact: true
  },
  {
    path: '/markdown-page/',
    component: ComponentCreator('/markdown-page/', 'd16'),
    exact: true
  },
  {
    path: '/docs/',
    component: ComponentCreator('/docs/', '029'),
    routes: [
      {
        path: '/docs/category/examples/',
        component: ComponentCreator('/docs/category/examples/', 'f3e'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/intro/',
        component: ComponentCreator('/docs/intro/', '688'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/tutorial-basics/231/',
        component: ComponentCreator('/docs/tutorial-basics/231/', 'e76'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/tutorial-basics/samplesequence/',
        component: ComponentCreator('/docs/tutorial-basics/samplesequence/', '23d'),
        exact: true,
        sidebar: "tutorialSidebar"
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', '8bf'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
