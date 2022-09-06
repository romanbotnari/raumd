import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGlobe, faBridgeWater, faUserAstronaut } from '@fortawesome/free-solid-svg-icons'


const FeatureList = [
  {
    title: 'Harmonization',
    img: faBridgeWater,
    description: (
      <>
        Standardize the operations whithin your projects with raumd as an abstraction layer that hides the underlying complexity and peculiarities.
      </>
    ),
  },
  {
    title: 'Accessibility',
    img: faGlobe,
    description: (
      <>
        Upload your shell commands or scripts to <a href="https://airlocks.xyz">airlocks</a> and download them wherever you need, to have a seamless transition from one env to another.
      </>
    ),
  },
  {
    title: 'Customization',
    img: faUserAstronaut,
    description: (
      <>
        Create your own way of interacting with the tool, choosing your language as well as the structure based on the tree's of operations you can navigate through.
      </>
    ),
  },
];

function Feature({img, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <FontAwesomeIcon icon={img} className={styles.featureSvg}/>
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
