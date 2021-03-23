import '../styles/globals.css'
import App, { Container } from 'next/app';
import React from 'react';
import { getStores, StoreProvider } from '../stores/stores';
import { Provider } from 'mobx'


class MyApp extends App{
  static async getInitialProps(appContext) {
    const mobxStores = getStores();
    appContext.ctx.mobxStores = mobxStores;
    const appProps = await App.getInitialProps(appContext);
    
    const initialData = {
      postStoreInitialData: null
    };
    
    return {
      ...appProps,
      initialData,
    };

  }

  render() {
    const { Component, pageProps, initialData } = this.props;
    const stores = getStores(initialData);
    return (
      <StoreProvider value={stores}>
        <Container>
          <Component {...pageProps} />
        </Container>
      </StoreProvider>
    );
  }
  
}

export default MyApp
